import { useParams } from 'react-router-dom';
import { useQuery } from '@tanstack/react-query';
import { formatDate } from '@/utils/formatTime';
import { fetchNewsById } from '@/lib/fetcher';
import type { News } from '@/types/type';


export default function News() {

  const { id } = useParams<{ id: string }>();
  console.log('id:', id, typeof id);


  const { data: news, isLoading, isError, error } = useQuery<News>({
    queryKey: ['news', id],
    queryFn: () => fetchNewsById(Number(id)),
    enabled: !!id,
  });

  if (isLoading) {
    return <div className="text-center py-20">Loading...</div>;
  }

  if (isError || !news) {
    return <div className="text-center py-20">Loading failed: {error?.message}</div>;
  }

  return (
    <main className='container mx-auto max-w-2xl'>
      {/* Article */}
      <article className='my-4 mx-4'>
        <h1 className='font-serif text-center text-3xl mb-4'>{news.title}</h1>
        <time className='text-gray-700 text-sm'>{formatDate(news.created_at)}</time>
        <p className='whitespace-pre-wrap mt-4'>{news.contents_main}</p>
      </article>
      {/* Lightbox */}
      <figure className="mx-4">
        <input type="checkbox" id='lightbox' className="peer hidden" />
        <label htmlFor='lightbox'>
          <img
            src={news.images[0]?.image}
            alt={news.images[0]?.caption || 'Image'} />
        </label>
        <label htmlFor='lightbox'
          className="peer-checked:flex hidden fixed inset-0 bg-black/70 justify-center items-center">
          <img
            src={news.images[0]?.image}
            alt={news.images[0]?.caption || 'Image'}
            className='max-h-[95vh] object-contain' />
        </label>
      </figure>
    </main >
  )
}