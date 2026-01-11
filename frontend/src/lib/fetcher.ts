export const fetchBanners = async () => {
  const res = await fetch('/api/banners/');
  if (!res.ok) throw new Error('Failed to fetch banners');
  return res.json();
};

export const fetchNews = async () => {
  const res = await fetch('/api/news/');
  if (!res.ok) throw new Error('Failed to fetch news');
  return res.json();
};

export const fetchNewsById = async (id: number) => {
  const res = await fetch(`/api/news/${id}/`);
  if (!res.ok) throw new Error('Failed to fetch news detail');
  return res.json();
};

export const fetchNotice = async () => {
  const res = await fetch('/api/notices/');
  if (!res.ok) throw new Error('Failed to fetch notice');
  return res.json();
};

export const fetchNoticeById = async (id: number) => {
  const res = await fetch(`/api/notices/${id}/`);
  if (!res.ok) throw new Error('Failed to fetch notice detail');
  return res.json();
};

export const fetchQuotes = async () => {
  const res = await fetch('/api/quotes/');
  if (!res.ok) throw new Error('Failed to fetch quotes');
  return res.json();
};