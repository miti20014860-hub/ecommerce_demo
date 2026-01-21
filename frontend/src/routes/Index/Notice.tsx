import { useParams } from 'react-router-dom';
import { useQuery } from '@tanstack/react-query';
import { formatDate } from '@/utils/formatTime';
import { fetchNoticeById } from '@/lib/fetcher';
import type { Notice } from '@/types/type';
import Map from '@/components/Map';

export default function Notice() {

  const { id } = useParams<{ id: string }>();

  const { data: notice, isLoading, isError, error } = useQuery<Notice>({
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
    <main className='container mx-auto max-w-3xl'>
      {/* Article */}
      <article className='my-6 mx-4'>
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
        <section className='mx-3'>
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