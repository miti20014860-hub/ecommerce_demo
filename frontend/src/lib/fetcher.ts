import type { Banner, News, Notice, Quote, Activity, Booking } from '@/types/type';

// Index
export const fetchBanners = async (): Promise<Banner[]> => {
  const res = await fetch('/api/banners/');
  if (!res.ok) throw new Error(`Failed to fetch banners: ${res.status} ${res.statusText}`);
  return res.json();
};

export const fetchNews = async (): Promise<News[]> => {
  const res = await fetch('/api/news/');
  if (!res.ok) throw new Error(`Failed to fetch news: ${res.status} ${res.statusText}`);
  return res.json();
};

export const fetchNewsById = async (id: number): Promise<News> => {
  const res = await fetch(`/api/news/${id}/`);
  if (!res.ok) throw new Error(`Failed to fetch news detail: ${res.status} ${res.statusText}`);
  return res.json();
};

export const fetchNotice = async (): Promise<Notice[]> => {
  const res = await fetch('/api/notices/');
  if (!res.ok) throw new Error(`Failed to fetch notices: ${res.status} ${res.statusText}`);
  return res.json();
};

export const fetchNoticeById = async (id: number): Promise<Notice> => {
  const res = await fetch(`/api/notices/${id}/`);
  if (!res.ok) throw new Error(`Failed to fetch notice detail: ${res.status} ${res.statusText}`);
  return res.json();
};

export const fetchQuotes = async (): Promise<Quote[]> => {
  const res = await fetch('/api/quotes/');
  if (!res.ok) throw new Error(`Failed to fetch quotes: ${res.status} ${res.statusText}`);
  return res.json();
};

// Activity
export const fetchActivity = async (): Promise<Activity[]> => {
  const res = await fetch('/api/activities/');
  if (!res.ok) throw new Error(`Failed to fetch activities: ${res.status} ${res.statusText}`);
  return res.json();
};

export const fetchActivityById = async (id: number): Promise<Activity> => {
  const res = await fetch(`/api/activities/${id}/`);
  if (!res.ok) throw new Error(`Failed to fetch activity detail: ${res.status} ${res.statusText}`);
  return res.json();
};

export const fetchBooking = async (): Promise<Booking[]> => {
  const res = await fetch('/api/bookings/');
  if (!res.ok) throw new Error(`Failed to fetch bookings: ${res.status} ${res.statusText}`);
  return res.json();
};