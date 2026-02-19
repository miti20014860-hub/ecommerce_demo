import { useParams } from 'react-router-dom';
import { useQuery } from '@tanstack/react-query';
import { formatDate } from '@/utils/formatTime';
import { fetchNoticeById } from '@/lib/fetcher';
import Map from '@/components/partials/Map';

export const Notice = () => {

  const { id } = useParams<{ id: string }>();
  const { data: notice, isLoading, isError, error } = useQuery({
    queryKey: ['notice', id],
    queryFn: () => fetchNoticeById(Number(id)),
    enabled: !!id,
  });

  if (isLoading) {
    return <div className='text-center py-20'>Loading...</div>;
  }

  if (isError || !notice) {
    return <div className='text-center py-20'>Loading failed: {error?.message}</div>;
  }

  return (
    <main className='container mx-auto sm:px-8 md:px-16 lg:px-32 xl:px-64 2xl:px-96'>
      {/* Article */}
      <article className='mt-6 mx-4'>
        <h1 className='font-serif text-center text-4xl mb-4'>{notice.title}</h1>
        <time className='text-gray-700 text-sm'>{formatDate(notice.created_at)}</time>
        <p className='whitespace-pre-wrap my-5'>{notice.contents_main}</p>
        <h2 className='font-medium bg-gray-200 text-3xl mb-4'>{notice.subtitle_1}</h2>
        <p className='whitespace-pre-wrap my-5'>{notice.contents_1}</p>
        <h2 className='font-medium bg-gray-200 text-3xl mb-4'>{notice.subtitle_2}</h2>
        <p className='whitespace-pre-wrap my-5'>{notice.contents_2}</p>
      </article>

      {/* Map */}
      {notice.lat && notice.lng && (
        <section className='mx-4'>
          <Map
            lat={notice.lat}
            lng={notice.lng}
            address={notice.address}
            zoom={15}
            height='400px'
          />
        </section>
      )}
    </main >
  )
}

export default Notice
