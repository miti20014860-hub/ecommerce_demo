import { useQuery } from '@tanstack/react-query';
import { useState } from 'react';
import axios from 'axios';
import ActivityFilters from '@/components/ActivityFilters';
import type { ActivityProps, ActivityFilterOptions, ActivityFilterState, PaginatedResponse } from '@/types/type';

const INITIAL_FILTERS: ActivityFilterState = {
  q: '',
  types: [],
  charge_min: '',
  charge_max: '',
  event_ends: '',
  prefectures: [],
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

  const { data: activities, isLoading: isListLoading } = useQuery<PaginatedResponse<ActivityProps>>({
    queryKey: ['activities', filters],
    queryFn: async () => {
      const params = new URLSearchParams();
      Object.entries(filters).forEach(([key, value]) => {
        if (Array.isArray(value)) {
          value.forEach(v => {
            if (v) params.append(key, v);
          });
        } else if (value !== '' && value !== null && value !== undefined) {
          params.append(key, String(value));
        }
      });
      const res = await axios.get('/api/activities/', { params });
      return res.data;
    },
  });

  return (
    <main className='container mx-auto lg:px-8 xl:px-16 2xl:px-24 flex flex-col lg:flex-row gap-6 py-6'>
      {/* Button */}
      <button
        onClick={() => setIsOpen(true)}
        className="lg:hidden fixed bottom-6 right-6 bg-blue-600 text-white px-6 py-3 rounded-full shadow-2xl flex items-center gap-2 z-40 active:scale-95 transition-transform"
      >
        <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z" /></svg>
        Filters
      </button>

      {/* Sidebar */}
      <aside
        className={`
          w-[300px] flex-shrink-0 bg-white
          fixed inset-y-0 left-0 z-50 shadow-xl transition-transform duration-300 ease-in-out
          lg:relative lg:translate-x-0 lg:shadow-none lg:z-auto
          ${isOpen ? 'translate-x-0' : '-translate-x-full'}
        `}
      >
        <ActivityFilters
          options={filterOptions}
          filters={filters}
          setFilters={setFilters}
          onClear={() => setFilters(INITIAL_FILTERS)}
          isLoading={isOptionsLoading}
        />
      </aside>

      {/* List */}
      <div className='flex-1 min-w-0'>
        <div className="mb-4 flex justify-between items-end">
          <h2 className="text-xl font-bold text-slate-800">
            {isListLoading ? 'Searching...' : `${activities?.count || 0} Activities Found`}
          </h2>
          {filters.q && (
            <span className="text-sm text-slate-500">
              Results for <span className="font-semibold text-blue-600">"{filters.q}"</span>
            </span>
          )}
        </div>

        {isListLoading ? (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {[...Array(4)].map((_, i) => (
              <div key={i} className="h-64 bg-slate-100 animate-pulse rounded-2xl" />
            ))}
          </div>
        ) : (
          <>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {activities?.results?.map((item) => (
                <article key={item.id} className="group bg-white border border-slate-200 p-5 rounded-2xl shadow-sm hover:shadow-md transition-shadow">
                  {/* Detail */}
                  <div className="text-xs text-blue-600 font-bold uppercase mb-1">{item.type}</div>
                  <h3 className="font-bold text-lg group-hover:text-blue-600 transition-colors">{item.title}</h3>
                  <div className="mt-4 flex justify-between items-center">
                    <span className="text-lg font-black">{item.currency} {item.minimum_charge}</span>
                    <button className="text-sm bg-slate-100 px-4 py-2 rounded-lg font-medium">Details</button>
                  </div>
                </article>
              ))}
            </div>

            {activities?.results?.length === 0 && (
              <div className="py-20 text-center bg-slate-50 rounded-3xl border-2 border-dashed border-slate-200">
                <p className="text-slate-400">No activities match your filters.</p>
                <button
                  onClick={() => setFilters(INITIAL_FILTERS)}
                  className="mt-2 text-blue-600 font-medium hover:underline"
                >
                  Clear all filters
                </button>
              </div>
            )}
          </>
        )}
      </div>

      {/* Mask */}
      {isOpen && (
        <div className="fixed inset-0 bg-slate-900/40 backdrop-blur-sm lg:hidden z-30" onClick={() => setIsOpen(false)} />
      )}
    </main>
  );
};

export default Activity;