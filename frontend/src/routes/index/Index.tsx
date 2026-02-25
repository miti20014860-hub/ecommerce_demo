import { Link, useLocation } from 'react-router-dom';
import { useQueries } from '@tanstack/react-query';
import { naturalTime, formatDate } from '@/utils/formatTime';
import { fetchBanners, fetchNews, fetchNotices, fetchQuotes } from '@/lib/fetcher';

export const Index = () => {
  const location = useLocation();
  const pathname = location.pathname;
  const isCurrent = (path: string) => {
    return pathname.startsWith(path);
  };

  const results = useQueries({
    queries: [
      { queryKey: ['banners'], queryFn: fetchBanners },
      { queryKey: ['news'], queryFn: fetchNews },
      { queryKey: ['notice'], queryFn: fetchNotices },
      { queryKey: ['quotes'], queryFn: fetchQuotes },
    ],
  });

  const [bannersQuery, newsQuery, noticesQuery, quotesQuery] = results;

  const { data: banners = [], isLoading: bannersLoading, isError: bannersHasError, error: bannersError } = bannersQuery;
  const { data: news = [], isLoading: newsLoading, isError: newsHasError, error: newsError } = newsQuery;
  const { data: notices = [], isLoading: noticesLoading, isError: noticesHasError, error: noticesError } = noticesQuery;
  const { data: quotes = [], isLoading: quotesLoading, isError: quotesHasError, error: quotesError } = quotesQuery;

  const isLoading = bannersLoading || newsLoading || noticesLoading || quotesLoading;
  const isError = bannersHasError || newsHasError || noticesHasError || quotesHasError;
  const error = bannersError || newsError || noticesError || quotesError;

  const featuredNews = news.filter((item) => item.is_featured).slice(0, 2);
  const recentNews = news.filter((item) => !item.is_featured).slice(0, 4);

  if (isLoading) {
    return <div className='text-center py-20'>Loading...</div>;
  }

  if (isError) {
    return <div className='text-center py-20'>Loading failed: {error?.message}</div>;
  }

  return (
    <main className='container mx-auto 2xl:px-24'>
      {/* Banner */}
      <figure className='mb-2'>
        {banners.map((banner) => (
          <Link to='/kenshi/'
            key={banner.id}
            aria-current={isCurrent('/kenshi/') ? 'page' : undefined}>
            <img
              key={banner.id}
              src={banner.image}
              alt={banner.caption || 'Banner'}
              className='w-full' />
          </Link>
        ))}
      </figure>

      {/* Featured News */}
      <section className='grid lg:grid-cols-2 mb-2'>
        {featuredNews.map((news) => (
          <div key={news.id} className='lg:col-span-1 border border-gray-200 shadow-md rounded-s-lg mx-2 my-1'>
            <article className='relative grid grid-cols-5 w-full h-full'>
              <div className='col-span-3 p-5 mb-1'>
                <h2 className='font-serif line-clamp-2 text-2xl'>{news.title}</h2>
                <time className='text-gray-700'>{naturalTime(news.created_at)}</time>
                <p className='line-clamp-2 lg:line-clamp-3 2xl:line-clamp-4 mb-6 mt-1'>{news.contents_main}</p>
                <Link to={`/news/${news.id}/`}
                  className='absolute bottom-4 underline text-gray-500 hover:text-gray-700'
                  aria-current={isCurrent(`/news/${news.id}/`) ? 'page' : undefined}>
                  Continue reading »
                </Link>
              </div>
              <div className='relative col-span-2'>
                <Link to={`/news/${news.id}/`}
                  aria-current={isCurrent(`/news/${news.id}/`) ? 'page' : undefined}>
                  <img
                    src={news.images[0]?.image}
                    alt={news.images[0]?.caption || 'Thumbnail'}
                    className='absolute w-full h-full object-cover' />
                </Link>
              </div>
            </article>
          </div>
        ))}
      </section>
      <div className='grid lg:grid-cols-3'>

        {/* Notices */}
        <div className='lg:col-span-2'>
          {notices.map((notice) => (
            <article key={notice.id} className='p-3 mt-3 mx-2'>
              <h2 className='font-serif text-2xl'>{notice.title}</h2>
              <time className='text-gray-700'>{formatDate(notice.created_at)}</time>
              <p className='line-clamp-2 my-3'>{notice.contents_main}</p>
              <Link to={`/notice/${notice.id}/`}
                className='underline text-gray-500 hover:text-gray-700'
                aria-current={isCurrent(`/notice/${notice.id}/`) ? 'page' : undefined}>
                Continue reading »
              </Link>
              <hr className='text-gray-400 mt-6' />
            </article>
          ))}
        </div>
        <aside className='lg:col-span-1 px-2'>

          {/* Quote */}
          {quotes.map((quote) => (
            <div key={quote.id} className='bg-gray-50 p-3 mt-2'>
              <p className='font-serif text-lg mb-2' >{quote.content}</p>
              <p className='font-serif text-end'>{quote.author}</p>
            </div>
          ))}

          {/* Recent news */}
          <h4 className='italic text-2xl mt-5 ms-2'>Recent news</h4>
          {recentNews.map((news) => (
            <article key={news.id} className='grid grid-cols-3 border-t border-gray-400 mt-3 p-1'>
              <Link to={`/news/${news.id}/`}
                className='relative min-h-30 col-span-1 mt-4'
                aria-current={isCurrent(`/news/${news.id}/`) ? 'page' : undefined}>
                <img
                  src={news.images[0]?.image}
                  alt={news.images[0]?.caption || 'Thumbnail'}
                  className='absolute w-full h-full object-cover'
                />
              </Link>
              <div className='col-span-2 ms-1 mt-3 p-2'>
                <Link to={`/news/${news.id}/`}
                  className='line-clamp-1 font-serif hover:text-gray-700'
                  aria-current={isCurrent(`/news/${news.id}/`) ? 'page' : undefined}>
                  {news.title}
                </Link>
                <time className='text-sm text-gray-700'>{naturalTime(news.created_at)}</time>
                <p className='line-clamp-2 text-sm mt-2'>{news.contents_main}</p>
              </div>
            </article>
          ))}
        </aside>
      </div>
    </main >
  )
}

export default Index
