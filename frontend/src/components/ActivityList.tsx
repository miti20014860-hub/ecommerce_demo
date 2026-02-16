import { Link, useLocation } from 'react-router-dom';
import Pagination from '@/components/Pagination';
import type { Activity, PaginatedResponse } from '@/types/type';

interface ActivityListProps {
  data?: PaginatedResponse<Activity>;
  isLoading: boolean;
  currentPage: number;
  onPageChange: (page: number) => void;
}

export const ActivityList = ({ data, isLoading, currentPage, onPageChange }: ActivityListProps) => {
  const location = useLocation();
  const pathname = location.pathname;
  const isCurrent = (path: string) => {
    return pathname.startsWith(path);
  };
  if (isLoading) return <div className='animate-pulse text-slate-400 text-center py-20'>Loading List...</div>;
  if (!data || data.results.length === 0) {
    return <div className='text-center text-slate-500 py-20'>No activities found.</div>;
  }
  return (
    <div className='lg:ms-1'>
      {/* List */}
      {data.results.map((activity) => (
        <div key={activity.id} className='group border border-t-4 border-slate-400 hover:border-gray-500 hover:shadow-lg transition-shadow duration-300 overflow-hidden px-3 mb-3 '>
          {/* Title */}
          <Link to={`/activity/${activity.id}/`}
            aria-current={isCurrent(`/activity/${activity.id}/`) ? 'page' : undefined}>
            <h3 className='text-2xl font-serif my-3'>
              {activity.title}
            </h3>
          </Link>
          {/* Content */}
          <div className='grid lg:grid-cols-12 border-t-2 border-slate-300 group-hover:border-gray-400 '>
            {/* Image */}
            <div className='h-60 my-2 overflow-hidden lg:col-span-5'>
              <Link to={`/activity/${activity.id}/`}
                aria-current={isCurrent(`/activity/${activity.id}/`) ? 'page' : undefined}>
                <img
                  src={activity.images[0]?.image}
                  alt={activity.title || 'Thumbnail'}
                  className='w-full h-full object-cover group-hover:scale-105 transition-transform duration-300'
                />
              </Link>
            </div>
            {/* Description */}
            <div className='flex flex-col my-3 lg:ps-3 lg:col-span-7'>
              <div className='flex gap-2'>
                <span className='bg-cyan-400 rounded text-sm px-2 py-1'>{activity.prefecture_display}</span>
                <span className='bg-yellow-400 rounded text-sm px-2 py-1'>{activity.type_display}</span>
              </div>
              <p className='text-sm text-slate-500 line-clamp-6 p-1 mt-2 mb-auto'>{activity.description}</p>
              <Link to={`/activity/${activity.id}/`}
                aria-current={isCurrent(`/activity/${activity.id}/`) ? 'page' : undefined}
                className='w-full rounded-md bg-rose-600 text-center text-white font-semibold py-1.5 mt-4 transition-color duration-300 hover:bg-rose-500'>
                {Number(activity.minimum_charge) === 0 ? 'Free' : `${Number(activity.minimum_charge).toLocaleString()} ${activity.currency} ～`}
              </Link>
            </div>
          </div>
        </div>
      ))}

      {/* Pagination */}
      <Pagination
        current={currentPage}
        totalCount={data.count}
        pageSize={6}
        onPageChange={onPageChange}
      />
    </div>
  );
};

export default ActivityList;