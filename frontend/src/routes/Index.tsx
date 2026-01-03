import { useQueries } from '@tanstack/react-query';
import { fetchBanners, fetchQuotes } from '../lib/fetcher';
import type { Banner, Quote } from '../types/type';


export default function Index() {

  const results = useQueries({
    queries: [
      { queryKey: ['banners'], queryFn: fetchBanners },
      { queryKey: ['quotes'], queryFn: fetchQuotes },
    ],
  });

  const [bannersQuery, quotesQuery] = results as [
    { data: Banner[] | undefined; isLoading: boolean; isError: boolean; error: Error | null },
    { data: Quote[] | undefined; isLoading: boolean; isError: boolean; error: Error | null }
  ];

  const { data: banners = [], isLoading: bannersLoading, isError: bannersHasError, error: bannersError } = bannersQuery;
  const { data: quotes = [], isLoading: quotesLoading, isError: quotesHasError, error: quotesError } = quotesQuery;

  const isLoading = bannersLoading || quotesLoading;
  const isError = bannersHasError || quotesHasError;
  const error = bannersError || quotesError;

  if (isLoading) {
    return <div className="text-center py-20">Loading...</div>;
  }

  if (isError) {
    return <div className="text-center py-20">Loading failed: {error?.message}</div>;
  }

  return (
    <main className="container mx-auto">
      {/* Banner */}
      {banners.map((banner) => (
        <a
          href="/"
          role="button"
          aria-label="to Kenshi">
          <img
            key={banner.id}
            src={banner.image}
            alt={banner.caption || "Banner"}
            className="w-full" />
        </a>
      ))}
      {/* Featured newses */}
      <section className="grid lg:grid-cols-2 bg-green-500">
        <div className="lg:col-span-1">
          <div className="col p-4 d-flex flex-column">
            <h4 className="mb-0">news.title</h4>
            <div className="my-1 text-body-secondary">news.created_at | naturaltime</div>
            <p className="card-text mb-auto">news.contents_main | striptags | truncatewords:12</p>
            <a href="{% url 'index:news' news.pk %}"
              className="link-body-emphasis text-secondary">Continue reading »</a>
          </div>
          <a href="{% url 'index:news' news.pk %}" className="col-5">
            <img src="{% if news.main_image_url %}news.main_image_url{% else %}{% static 'img/default-news.jpg' %}{% endif %}"
              className="object-fit-cover"
              alt="Thumbnail"
              width="100%"
              height="240" />
          </a>
        </div>
      </section>
      {/* Notices */}
      <section className="grid lg:grid-cols-3 bg-red-400">
        <article className="lg:col-span-2">
          <h4 className="">notice.title</h4>
          <p>notice.created_at | date:"F j, Y"</p>
          <div className="">
            <p>
              notice.contents_1 | striptags | truncatewords:30
              No content available.
            </p>
          </div>
          <a href="{% url 'index:notice' notice.pk %}"
            className="">Continue reading »</a>
        </article>
        {/* Quote */}
        <aside className="bg-blue-400">
          <div className="p-3 mb-3 bg-body-tertiary rounded">
            {quotes.map((quote) => (
              <div key={quote.id}>
                <p className="mb-2" >{quote.content}</p>
                <p className="text-end my-0">{quote.author}</p>
              </div>
            ))}
          </div>
          {/* Recent news */}
          <ul className="list-unstyled ms-3">
            <h4 className="fst-italic">Recent news</h4>
            <li>
              <div className="row py-3 border-top">
                <a href="{% url 'index:news' news.pk %}" className="col-4">
                  <img src="{% if news.main_image_url %}news.main_image_url{% else %}{% static 'img/default-news.jpg' %}{% endif %}"
                    className="object-fit-cover"
                    alt="news.title"
                    width="100%"
                    height="100" />
                </a>
                <div className="col g-0 pt-1 me-4 d-flex flex-column">
                  <a href="{% url 'index:news' news.pk %}"
                    className="text-decoration-none link-body-emphasis text-black">
                    <h6 className="mb-0">news.title</h6>
                  </a>
                  <small className="text-body-secondary">news.contents_main | truncatewords:12</small>
                </div>
              </div>
            </li>
            <li>
              <p className="text-muted">No news</p>
            </li>
          </ul>
        </aside>
      </section>
    </main >

  )
}