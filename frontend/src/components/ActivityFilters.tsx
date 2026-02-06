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
    <div className="border-b border-slate-200 py-4">
      <button
        type="button"
        onClick={() => setIsOpen(!isOpen)}
        className="flex w-full justify-between ms-1"
      >
        <span className="text-xs tracking-wider font-bold uppercase">{title}</span>
        <ChevronDown className={`h-4 w-4 me-1 transition-transform duration-200 ${isOpen ? 'rotate-180' : ''}`} />
      </button>
      <div className={`grid transition-all duration-300 ease-in-out ${isOpen ? 'grid-rows-[1fr] opacity-100 mt-3 pb-2' : 'grid-rows-[0fr] opacity-0'}`}>
        <div className="overflow-hidden">
          <div className="flex flex-col gap-2 text-sm text-slate-600 mx-1">
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
      return { ...prev, q: debouncedValue };
    });
  }, [debouncedValue, setFilters]);

  const handleInternalClear = () => {
    setLocalSearch('');
    onClear();
    if (inputRef.current) {
      inputRef.current.value = '';
    }
  };

  if (!options && isLoading) return <div className="animate-pulse text-slate-400 p-6">Loading Filters...</div>;

  return (
    <aside className="w-full flex flex-col h-full bg-white">
      {/* Search */}
      <div className="relative border-b border-slate-200 bg-slate-50/50 p-4">
        <Search className="absolute text-slate-400 left-7.5 top-6.5 w-4 h-4" />
        <input
          ref={inputRef}
          type="text"
          defaultValue={localSearch}
          onChange={(e) => setLocalSearch(e.target.value)}
          placeholder="Search activities..."
          className="w-full pl-9 pr-4 py-2 bg-white border border-slate-200 rounded-full text-sm focus:ring-2 focus:ring-blue-500 outline-none"
        />
      </div>

      {/* Sections */}
      <div className="flex-1 overflow-y-auto px-4 custom-scrollbar">
        {/* Type */}
        <FilterSection title="Type">
          <div className="flex flex-col gap-2">
            {options?.types.map((type) => (
              <label key={type.value} className="flex group items-center gap-3 cursor-pointer">
                <input
                  type="checkbox"
                  checked={filters.types.includes(type.value)}
                  onChange={(e) => {
                    const next = e.target.checked
                      ? [...filters.types, type.value]
                      : filters.types.filter((t) => t !== type.value);
                    setFilters({ ...filters, types: next });
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
            <div className="space-y-1">
              <span className="text-[10px] text-slate-400 uppercase">Min</span>
              <input
                type="number"
                value={filters.charge_min}
                onChange={(e) => setFilters({ ...filters, charge_min: e.target.value })}
                className="w-full border border-slate-200 rounded-md p-2 text-sm focus:border-blue-600 outline-none"
              />
            </div>
            <div className="space-y-1">
              <span className="text-[10px] text-slate-400 uppercase">Max</span>
              <input
                type="number"
                value={filters.charge_max}
                onChange={(e) => setFilters({ ...filters, charge_max: e.target.value })}
                className="w-full border border-slate-200 rounded-md p-2 text-sm focus:border-blue-600 outline-none"
              />
            </div>
          </div>
        </FilterSection>

        {/* Until */}
        <FilterSection title="Until">
          <input
            type="date"
            value={filters.event_ends}
            onChange={(e) => setFilters({ ...filters, event_ends: e.target.value })}
            className="w-full border border-slate-200 rounded-md p-2 text-sm focus:border-blue-600 outline-none"
          />
        </FilterSection>

        {/* Region */}
        <FilterSection title="Region" defaultOpen={false}>
          <div className="space-y-3 pt-1">
            {options?.region_groups.map((group) => (
              <div key={group.label} className="space-y-1">
                <h4 className="text-[10px] text-slate-400 font-bold uppercase tracking-widest">{group.label}</h4>
                <div className="flex flex-wrap gap-1.5">
                  {group.prefectures.map((pref) => (
                    <button
                      key={pref.value}
                      type="button"
                      onClick={() => {
                        const isSelected = filters.prefectures.includes(pref.value);
                        const next = isSelected
                          ? filters.prefectures.filter((p) => p !== pref.value)
                          : [...filters.prefectures, pref.value];
                        setFilters({ ...filters, prefectures: next });
                      }}
                      className={`px-2 py-1 text-xs rounded-md border transition-all ${filters.prefectures.includes(pref.value)
                        ? 'bg-blue-500 border-blue-500 text-white shadow-sm'
                        : 'bg-white border-slate-200 text-slate-600 hover:border-blue-500 hover:text-blue-500'
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
      </div>

      {/* Reset */}
      <div className="p-4 border-t border-slate-200">
        <button
          type="button"
          onClick={handleInternalClear}
          className="w-full py-3 text-xs font-bold uppercase tracking-wider text-slate-500 border border-slate-200 rounded-xl hover:bg-slate-50 hover:text-slate-700 transition-colors flex items-center justify-center gap-2"
        >
          Reset All Filters
        </button>
      </div>
    </aside>
  );
};

export default ActivityFilters;