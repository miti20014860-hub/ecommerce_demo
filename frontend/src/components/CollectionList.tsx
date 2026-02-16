import { Link, useLocation } from 'react-router-dom';
import Pagination from '@/components/Pagination';
import type { Collection, PaginatedResponse } from '@/types/type';

interface CollectionListProps {
  data?: PaginatedResponse<Collection>;
  isLoading: boolean;
  currentPage: number;
  onPageChange: (page: number) => void;
}

export const CollectionList = ({ data, isLoading, currentPage, onPageChange }: CollectionListProps) => {
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
      {data.results.map((collection) => (
        <div key={collection.id} className='group border border-t-4 border-gray-400 hover:border-gray-500 hover:shadow-lg transition-shadow duration-300 overflow-hidden px-3 mb-3'>
          <Link to={`/collection/${collection.id}/`}
            aria-current={isCurrent(`/collection/${collection.id}/`) ? 'page' : undefined}>
            {/* Title */}
            <h2 className='text-[23px] sm:text-[25px] md:text-[27px] text-center mt-4 underline text-yellow-900 xl:p-1 group-hover:text-yellow-700'>
              {collection.name_jp}
            </h2>
            {/* Image */}
            <img
              src={collection.images[0]?.image}
              alt={collection.name_en || 'Thumbnail'}
              className='w-full h-full object-cover group-hover:scale-102 transition-transform duration-300 mt-1 overflow-hidden'
            />
            <h2 className='text-[22px] sm:text-2xl md:text-[26px] font-medium text-center border-b-2 mb-4 p-1 xl:p-2 text-yellow-950 group-hover:text-yellow-800'>
              {Number(collection.price).toLocaleString()} {collection.currency}
            </h2>
          </Link>
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

export default CollectionList;