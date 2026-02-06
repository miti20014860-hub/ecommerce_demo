import { useParams } from 'react-router-dom';
import { useQuery } from '@tanstack/react-query';
import { formatDate } from '@/utils/formatTime';
import { fetchNewsById } from '@/lib/fetcher';

export const News = () => {

  const { id } = useParams<{ id: string }>();
  const { data: news, isLoading, isError, error } = useQuery({
    queryKey: ['news', id],
    queryFn: () => fetchNewsById(Number(id)),
    enabled: !!id,
  });

  if (isLoading) {
    return <div className='text-center py-20'>Loading...</div>;
  }

  if (isError || !news) {
    return <div className='text-center py-20'>Loading failed: {error?.message}</div>;
  }

  return (
    <main className='container mx-auto max-w-3xl'>
      {/* Article */}
      <article className='my-6 mx-4'>
        <h1 className='font-serif text-center text-4xl mb-4'>{news.title}</h1>
        <time className='text-gray-700 text-sm'>{formatDate(news.created_at)}</time>
        <p className='whitespace-pre-wrap mt-4'>{news.contents_main}</p>
      </article>

      {/* Lightbox */}
      <figure className='mx-4'>
        <input type='checkbox' id='lightbox' className='peer hidden' />
        <label htmlFor='lightbox'>
          <img
            src={news.images[0]?.image}
            alt={news.images[0]?.caption || 'Image'}
            className='w-full cursor-pointer' />
        </label>
        <div className='peer-checked:flex hidden fixed inset-0 bg-black/70 justify-center items-center'>
          <label
            htmlFor='lightbox'
            aria-label='Close'
            className='absolute inset-0' />
          <img
            src={news.images[0]?.image}
            alt={news.images[0]?.caption || 'Image'}
            className='relative max-w-[95vw] object-contain' />
        </div>
      </figure>
    </main >
  )
}

export default News
