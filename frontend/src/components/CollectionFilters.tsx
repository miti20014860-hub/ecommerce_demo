import { useState, useEffect, useRef } from 'react';
import { ChevronDown, Search } from 'lucide-react';
import { useDebounce } from 'use-debounce';
import type { CollectionFilterOptions, CollectionFilterState } from '@/types/type';

interface FilterSectionProps {
  title: string;
  children: React.ReactNode;
  defaultOpen?: boolean;
}

const FilterSection = ({
  title,
  children,
  defaultOpen = true
}: FilterSectionProps) => {
  const [isOpen, setIsOpen] = useState(defaultOpen);
  return (
    <div className="border-b border-slate-400 py-4">
      <button
        type="button"
        onClick={() => setIsOpen(!isOpen)}
        className="w-full flex justify-between ms-1 cursor-pointer"
      >
        <span className="text-xs font-bold tracking-wider uppercase">{title}</span>
        <ChevronDown className={`h-4 w-4 me-1 transition-transform duration-200 ${isOpen ? 'rotate-180' : ''}`} />
      </button>
      <div className={`grid transition-all duration-300 ease-in-out ${isOpen ? 'grid-rows-[1fr] opacity-100 mt-2' : 'grid-rows-[0fr] opacity-0'}`}>
        <div className="overflow-hidden">
          <div className="text-sm text-slate-600 mx-1">
            {children}
          </div>
        </div>
      </div>
    </div>
  );
};

interface CollectionFiltersProps {
  options?: CollectionFilterOptions;
  filters: CollectionFilterState;
  setFilters: React.Dispatch<React.SetStateAction<CollectionFilterState>>;
  onClear: () => void;
  isLoading?: boolean;
}

export const CollectionFilters = ({
  options,
  filters,
  setFilters,
  onClear,
  isLoading
}: CollectionFiltersProps) => {
  const [localSearch, setLocalSearch] = useState(filters.q);
  const [debouncedValue] = useDebounce(localSearch, 800);
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    setFilters(prev => {
      if (prev.q === debouncedValue) return prev;
      return { ...prev, q: debouncedValue, page: 1 };
    });
  }, [debouncedValue, setFilters]);

  const handleInternalClear = () => {
    setLocalSearch('');
    onClear();
    if (inputRef.current) {
      inputRef.current.value = '';
    }
  };

  if (!options && isLoading) return <div className="animate-pulse text-slate-400 text-center py-20">Loading Filters...</div>;

  return (
    <aside className="w-full h-full flex flex-col bg-white">
      {/* Search */}
      <div className="relative border-b border-slate-400 bg-slate-50/50 p-4">
        <Search className="absolute text-slate-400 left-7.5 top-6.5 w-4 h-4" />
        <input
          ref={inputRef}
          type="text"
          defaultValue={localSearch}
          onChange={(e) => setLocalSearch(e.target.value)}
          placeholder="Search activities..."
          className="w-full pl-9 py-2 bg-white border border-slate-400 rounded-full text-sm focus:ring-1 focus:ring-blue-500 outline-none"
        />
      </div>

      {/* Sections */}
      <div className="overflow-y-auto px-4">
        {/* Type */}
        <FilterSection title="Type">
          <div className="flex flex-col gap-2">
            {options?.types.map((type) => (
              <label key={type.value} className="group flex gap-3 items-center cursor-pointer">
                <input
                  type="checkbox"
                  checked={filters.types.includes(type.value)}
                  onChange={(e) => {
                    const next = e.target.checked
                      ? [...filters.types, type.value]
                      : filters.types.filter((t) => t !== type.value);
                    setFilters({ ...filters, types: next, page: 1 });
                  }}
                  className="w-4 h-4 cursor-pointer"
                />
                <span className="group-hover:text-blue-600 transition-colors">{type.label}</span>
              </label>
            ))}
          </div>
        </FilterSection>

        {/* Price */}
        <FilterSection title="Price">
          <div className="grid grid-cols-2 gap-3">
            <div className="col-span-1">
              <input
                type="number"
                value={filters.price_min}
                onChange={(e) => setFilters({ ...filters, price_min: e.target.value, page: 1 })}
                placeholder="Min"
                className="w-full border border-slate-400 rounded-md text-sm p-2 focus:border-blue-600 outline-none"
              />
            </div>
            <div className="col-span-1">
              <input
                type="number"
                value={filters.price_max}
                onChange={(e) => setFilters({ ...filters, price_max: e.target.value, page: 1 })}
                placeholder="Max"
                className="w-full border border-slate-400 rounded-md text-sm p-2 focus:border-blue-600 outline-none"
              />
            </div>
          </div>
        </FilterSection>

        {/* Period */}
        <FilterSection title="Period">
          <div className="flex flex-col gap-2">
            {options?.period_types.map((period) => (
              <label key={period.value} className="group flex gap-3 items-center cursor-pointer">
                <input
                  type="checkbox"
                  checked={filters.period_types.includes(period.value)}
                  onChange={(e) => {
                    const next = e.target.checked
                      ? [...filters.period_types, period.value]
                      : filters.period_types.filter((t) => t !== period.value);
                    setFilters({ ...filters, period_types: next, page: 1 });
                  }}
                  className="w-4 h-4 cursor-pointer"
                />
                <span className="group-hover:text-blue-600 transition-colors">{period.label}</span>
              </label>
            ))}
          </div>
        </FilterSection>

        {/* Length */}
        <FilterSection title="Length">
          <div className="grid grid-cols-2 gap-3">
            <div className="col-span-1">
              <input
                type="number"
                value={filters.length_min}
                onChange={(e) => setFilters({ ...filters, length_min: e.target.value, page: 1 })}
                placeholder="Min"
                className="w-full border border-slate-400 rounded-md text-sm p-2 focus:border-blue-600 outline-none"
              />
            </div>
            <div className="col-span-1">
              <input
                type="number"
                value={filters.length_max}
                onChange={(e) => setFilters({ ...filters, length_max: e.target.value, page: 1 })}
                placeholder="Max"
                className="w-full border border-slate-400 rounded-md text-sm p-2 focus:border-blue-600 outline-none"
              />
            </div>
          </div>
        </FilterSection>

        {/* Reset */}
        <div className="p-4">
          <button
            type="button"
            onClick={handleInternalClear}
            className="w-full py-3 text-xs text-slate-500 font-bold tracking-wider uppercase border border-slate-400 rounded-xl hover:bg-slate-50 hover:text-slate-600"
          >
            Reset All Filters
          </button>
        </div>
      </div>
    </aside>
  );
};

export default CollectionFilters;