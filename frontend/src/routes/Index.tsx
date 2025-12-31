import { useEffect, useState } from 'react'

interface Banner {
  id: number
  image: string
  caption: string
  is_active: boolean
}
interface Quotes {
  id: number
  author: string
  content: string
  is_featured: boolean
}

export default function Index() {
  const [banners, setBanners] = useState<Banner[]>([])
  const [quotes, setQuotes] = useState<Quote[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch('/api/quotes/')
      .then(res => {
        if (!res.ok) throw new Error('API ERROR')
        return res.json()
      })
      .then(data => {
        setQuotes(data)
        setLoading(false)
      })
      .catch(err => {
        console.error(err)
        setLoading(false)
      })
  }, [])
  useEffect(() => {
    fetch('/api/banner/')
      .then(res => res.json())
      .then(data => {
        console.log('Banner API 資料:', data);  // ← 關鍵！一定要看這裡
        setBanners(data);
      });
  }, []);

  if (loading) return <p className="text-center py-10">Loading...</p>

  return (
    // <div className="container mx-auto px-2 min-h-screen">
    //     <h1 className="text-4xl font-bold">Quotes API</h1>
    //     <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
    //         {quotes.map(quote => (
    //             <div key={quote.id} className="bg-white rounded-lg shadow p-6">
    //                 <p className="text-lg italic mb-4">「{quote.content}」</p>
    //                 <p className="text-right text-gray-600">— {quote.author}</p>
    //                 {quote.is_featured && <span className="inline-block mt-2 px-3 py-1 bg-yellow-200 text-yellow-800 rounded-full text-sm">Selected</span>}
    //             </div>
    //         ))}
    //     </div>
    // </div>
    <main className="container mx-auto">
      {/* Banner */}
      <section className="row">
        <div className="col g-0">
          {banners.map(banner => (
            <a
              key={banner.id}
              href="/"
              role="button"
              aria-label={banner.caption}>
              <img
                src={banner.image}
                alt={banner.caption}
                className="object-fit-cover"
                width="100%"
                height="100%" />
            </a>
          ))}
        </div>
      </section>
      {/* Featured newses */}
      <section className="row mt-2 mb-2">
        <article className="col-lg-6 mt-2{% if not forloop.first %} blog-post{% endif %}">
          <div className="row g-0 border rounded shadow-sm">
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
        </article>
        <article>
          <p className="text-muted">No news available.</p>
        </article>
      </section>
      <div className="row g-0">
        {/* Notices */}
        <section className="col-lg-8 g-4">
          <article className="{% if not forloop.first %}blog-post{% endif %}">
            <h4 className="mb-1">notice.title</h4>
            <p>notice.created_at | date:"F j, Y"</p>
            <div className="g-0">
              <p>
                notice.contents_1 | striptags | truncatewords:30
                No content available.
              </p>
            </div>
            <a href="{% url 'index:notice' notice.pk %}"
              className="link-body-emphasis text-secondary">Continue reading »</a>
            <hr />
          </article>
          <article>
            <p className="text-muted">No notices available.</p>
          </article>
        </section>
        {/* Recent news */}
        <section className="col-lg-4 mt-3">
          <div className="top-5">
            <aside className="p-3 mb-3 bg-body-tertiary rounded">
              <p className="mb-2">quote.content</p>
              <p className="text-end my-0">quote.author</p>
            </aside>
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
          </div>
        </section>
      </div>
    </main>

  )
}