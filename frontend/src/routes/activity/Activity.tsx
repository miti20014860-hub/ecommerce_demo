import { useQuery } from '@tanstack/react-query';
import { useState } from 'react';
import axios from 'axios';
import ActivityFilters from '@/components/ActivityFilters';
import ActivityList from '@/components/ActivityList';
import type { ActivityFilterOptions, ActivityFilterState } from '@/types/type';

const INITIAL_FILTERS: ActivityFilterState = {
  q: '',
  types: [],
  charge_min: '',
  charge_max: '',
  event_ends: '',
  prefectures: [],
  page: 1,
};

export const Activity = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [filters, setFilters] = useState<ActivityFilterState>(INITIAL_FILTERS);

  const { data: filterOptions, isLoading: isOptionsLoading } = useQuery<ActivityFilterOptions>({
    queryKey: ['activityFilters'],
    queryFn: async () => {
      const res = await axios.get('/api/activities/filters/');
      return res.data;
    },
    staleTime: 1000 * 60 * 30,
  });

  const { data: activities, isLoading: isListLoading } = useQuery({
    queryKey: ['activities', filters],
    queryFn: async () => {
      const params = new URLSearchParams();
      Object.entries(filters).forEach(([key, value]) => {
        if (Array.isArray(value)) {
          value.forEach(v => params.append(key, v));
        } else if (value) {
          params.append(key, String(value));
        }
      });
      const res = await axios.get('/api/activities/', { params });
      return res.data;
    }
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
        <ActivityFilters
          filters={filters}
          options={filterOptions}
          setFilters={setFilters}
          onClear={() => setFilters(INITIAL_FILTERS)}
          isLoading={isOptionsLoading}
        />
      </aside>

      {/* List */}
      <div className='flex-1 min-w-0'>
        <ActivityList
          data={activities}
          isLoading={isListLoading}
          currentPage={filters.page}
          onPageChange={(newPage) => setFilters({ ...filters, page: newPage })}
        />
      </div>

      {/* Mask */}
      {isOpen && (
        <div className='fixed inset-0 bg-slate-900/40 backdrop-blur-sm lg:hidden z-30' onClick={() => setIsOpen(false)} />
      )}
    </main>
  );
};

export default Activity;