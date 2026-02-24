import { useQuery } from '@tanstack/react-query';
import { useSearchParams } from 'react-router-dom';
import { useState, useMemo, useCallback } from 'react';
import { fetchCollections, fetchCollectionFilter } from '@/lib/fetcher';
import CollectionFilters from '@/components/collection/CollectionFilters';
import CollectionList from '@/components/collection/CollectionList';
import type { CollectionFilterOptions, CollectionFilterState } from '@/types/type';
import type { Dispatch, SetStateAction } from 'react';

export const Collection = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [searchParams, setSearchParams] = useSearchParams();

  const { data: filterOptions, isLoading: isOptionsLoading } = useQuery<CollectionFilterOptions>({
    queryKey: ['collectionFilters'],
    queryFn: () => fetchCollectionFilter(),
    staleTime: 1000 * 60 * 30,
  });

  const filters = useMemo(() => {
    return {
      q: searchParams.get('q') || '',
      types: searchParams.getAll('types'),
      price_min: searchParams.get('price_min') || '',
      price_max: searchParams.get('price_max') || '',
      period_types: searchParams.getAll('period_types') || '',
      length_min: searchParams.get('length_min'),
      length_max: searchParams.get('length_max'),
      page: Number(searchParams.get('page')) || 1,
    } as CollectionFilterState;
  }, [searchParams]);

  const updateFilters: Dispatch<SetStateAction<CollectionFilterState>> = useCallback((update) => {
    const nextFilters = typeof update === 'function' ? update(filters) : update;

    if (JSON.stringify(nextFilters) === JSON.stringify(filters)) {
      return;
    }

    const params = new URLSearchParams();
    Object.entries(nextFilters).forEach(([key, value]) => {
      if (Array.isArray(value)) {
        value.forEach(v => {
          if (v) params.append(key, String(v));
        });
      } else if (value !== undefined && value !== null && value !== '') {
        params.append(key, String(value));
      }
    });

    setSearchParams(params, { replace: true });
  }, [filters, setSearchParams]);

  const { data: collections, isLoading: isListLoading } = useQuery({
    queryKey: ['collections', filters],
    queryFn: () => fetchCollections(searchParams)
  });

  return (
    <main className='container mx-auto 2xl:px-24 flex lg:flex-row'>
      {/* Button */}
      <button
        onClick={() => setIsOpen(!isOpen)}
        className='lg:hidden fixed bottom-6 right-6 bg-gray-400 text-white px-6 py-3 rounded-full shadow-2xl flex items-center gap-2 z-40 active:scale-95 transition-transform'
      >
        <svg className='w-5 h-5' fill='none' viewBox='0 0 24 24' stroke='currentColor'><path strokeLinecap='round' strokeLinejoin='round' strokeWidth={2} d='M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z' /></svg>
        Filters
      </button>

      {/* Sidebar */}
      <aside
        className={`
          w-80 flex-shrink-0 bg-white
          fixed inset-y-0 left-0 z-50 shadow-xl transition-transform duration-300 ease-in-out
          lg:sticky lg:h-[calc(100vh-10rem)] lg:translate-x-0 lg:shadow-none lg:z-auto
          ${isOpen ? 'translate-x-0' : '-translate-x-full'}
        `}
      >
        <CollectionFilters
          filters={filters}
          options={filterOptions}
          setFilters={updateFilters}
          onClear={() => setSearchParams({})}
          isLoading={isOptionsLoading}
        />
      </aside>

      {/* List */}
      <div className='flex-1 min-w-0'>
        <CollectionList
          data={collections}
          isLoading={isListLoading}
          currentPage={filters.page}
          onPageChange={(newPage) => updateFilters({ ...filters, page: newPage })}
        />
      </div>

      {/* Mask */}
      {isOpen && (
        <div className='fixed inset-0 bg-slate-900/40 backdrop-blur-sm lg:hidden z-30' onClick={() => setIsOpen(false)} />
      )}
    </main>
  );
};

export default Collection;