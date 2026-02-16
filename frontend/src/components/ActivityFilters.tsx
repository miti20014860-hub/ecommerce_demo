import { useState, useEffect, useRef } from 'react';
import { ChevronDown, Search } from 'lucide-react';
import { useDebounce } from 'use-debounce';
import type { ActivityFilterOptions, ActivityFilterState } from '@/types/type';

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
    <div className="border-b border-slate-600 py-4">
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
          <div className="text-sm text-slate-800 mx-1">
            {children}
          </div>
        </div>
      </div>
    </div>
  );
};

interface ActivityFiltersProps {
  options?: ActivityFilterOptions;
  filters: ActivityFilterState;
  setFilters: React.Dispatch<React.SetStateAction<ActivityFilterState>>;
  onClear: () => void;
  isLoading?: boolean;
}

export const ActivityFilters = ({
  options,
  filters,
  setFilters,
  onClear,
  isLoading
}: ActivityFiltersProps) => {
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

  if (!options && isLoading) return <div className="animate-pulse text-slate-600 text-center py-20">Loading Filters...</div>;

  return (
    <aside className="w-full h-full flex flex-col bg-white">
      {/* Search */}
      <div className="relative border-b border-slate-600 bg-slate-50 p-4">
        <Search className="absolute text-slate-600 left-7.5 top-6.5 w-4 h-4" />
        <input
          ref={inputRef}
          type="text"
          defaultValue={localSearch}
          onChange={(e) => setLocalSearch(e.target.value)}
          placeholder="Search activities..."
          className="w-full pl-9 py-2 bg-white border border-slate-600 rounded-full text-sm focus:ring-1 focus:ring-blue-500 outline-none"
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
                value={filters.charge_min}
                onChange={(e) => setFilters({ ...filters, charge_min: e.target.value, page: 1 })}
                placeholder="Min"
                className="w-full border border-slate-600 rounded-md text-sm p-2 focus:border-blue-600 outline-none"
              />
            </div>
            <div className="col-span-1">
              <input
                type="number"
                value={filters.charge_max}
                onChange={(e) => setFilters({ ...filters, charge_max: e.target.value, page: 1 })}
                placeholder="Max"
                className="w-full border border-slate-600 rounded-md text-sm p-2 focus:border-blue-600 outline-none"
              />
            </div>
          </div>
        </FilterSection>

        {/* Until */}
        <FilterSection title="Until">
          <input
            type="date"
            value={filters.event_ends}
            onChange={(e) => setFilters({ ...filters, event_ends: e.target.value, page: 1 })}
            className="w-full border border-slate-600 rounded-md text-sm p-2 focus:border-blue-600 outline-none"
          />
        </FilterSection>

        {/* Region */}
        <FilterSection title="Region" defaultOpen={false}>
          <div className="space-y-3 mt-1">
            {options?.region_groups.map((region) => (
              <div key={region.label} className="space-y-1">
                <h4 className="text-xs text-slate-600 font-medium uppercase tracking-wide">{region.label}</h4>
                <div className="flex flex-wrap gap-1.5">
                  {region.prefectures.map((pref) => (
                    <button
                      key={pref.value}
                      type="button"
                      onClick={() => {
                        const isSelected = filters.prefectures.includes(pref.value);
                        const next = isSelected
                          ? filters.prefectures.filter((p) => p !== pref.value)
                          : [...filters.prefectures, pref.value];
                        setFilters({ ...filters, prefectures: next, page: 1 });
                      }}
                      className={`px-2 py-1 text-xs rounded-md border transition-all ${filters.prefectures.includes(pref.value)
                        ? 'bg-cyan-400 border-cyan-400 text-black shadow-sm'
                        : 'bg-white border-slate-600 text-slate-800 hover:border-blue-500 hover:text-blue-600'
                        }`}
                    >
                      {pref.label}
                    </button>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </FilterSection>

        {/* Reset */}
        <div className="p-4">
          <button
            type="button"
            onClick={handleInternalClear}
            className="w-full py-3 text-xs text-slate-500 font-bold tracking-wider uppercase border border-slate-600 rounded-xl hover:bg-slate-50 hover:text-slate-800"
          >
            Reset All Filters
          </button>
        </div>
      </div>
    </aside>
  );
};

export default ActivityFilters;