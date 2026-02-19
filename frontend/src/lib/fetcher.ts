import type { Banner, News, Notice, Quote, Activity, Booking, Collection, Order, Kenshi, MemberProfile, SignIn, SignUp, UpdateProfileRequest, ChangePasswordRequest } from '@/types/type';
import api from './api';
import axios from 'axios';

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

export const fetchNotices = async (): Promise<Notice[]> => {
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
export const fetchActivities = async (): Promise<Activity[]> => {
  const res = await fetch('/api/activities/');
  if (!res.ok) throw new Error(`Failed to fetch activities: ${res.status} ${res.statusText}`);
  return res.json();
};

export const fetchActivityById = async (id: number): Promise<Activity> => {
  const res = await fetch(`/api/activities/${id}/`);
  if (!res.ok) throw new Error(`Failed to fetch activity detail: ${res.status} ${res.statusText}`);
  return res.json();
};

export const createBooking = async (data: Partial<Booking>): Promise<Booking> => {
  try {
    const response = await api.post<Booking>('/bookings/', data);
    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      const serverMessage = error.response?.data?.detail || 'Booking failed. Please check your information.';
      throw new Error(serverMessage);
    }
    throw new Error('An unexpected error occurred');
  }
};

// Collection
export const fetchCollections = async (): Promise<Collection[]> => {
  const res = await fetch('/api/collections/');
  if (!res.ok) throw new Error(`Failed to fetch collections: ${res.status} ${res.statusText}`);
  return res.json();
};

export const fetchCollectionById = async (id: number): Promise<Collection> => {
  const res = await fetch(`/api/collections/${id}/`);
  if (!res.ok) throw new Error(`Failed to fetch collection detail: ${res.status} ${res.statusText}`);
  return res.json();
};

export const createOrder = async (data: Partial<Order>): Promise<Order> => {
  try {
    const response = await api.post<Order>('/orders/', data);
    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      const serverMessage = error.response?.data?.detail || 'Order failed. Please check your information.';
      throw new Error(serverMessage);
    }
    throw new Error('An unexpected error occurred');
  }
};

// Kenshi
export const fetchKenshi = async (): Promise<Kenshi[]> => {
  const res = await fetch('/api/kenshi/');
  if (!res.ok) throw new Error(`Failed to fetch kenshi: ${res.status} ${res.statusText}`);
  return res.json();
};

// Member
export const fetchMemberProfile = async (): Promise<MemberProfile> => {
  try {
    const { data } = await api.get<MemberProfile>('/profile/');
    return data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      if (error.response?.status === 401) {
        throw new Error('Please log in to view your profile.');
      }
    }
    throw new Error('Could not load profile. Please try again later.');
  }
};

export const signIn = async (credentials: SignIn) => {
  try {
    const response = await api.post('/sign_in/', credentials);
    const data = response.data;

    if (data.access) {
      localStorage.setItem('access_token', data.access);
      localStorage.setItem('refresh_token', data.refresh);
    }

    return data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      const serverMessage = error.response?.data?.detail;
      throw new Error(serverMessage || 'Invalid username or password');
    }

    if (error instanceof Error) {
      throw new Error(error.message);
    }

    throw new Error('An unexpected error occurred');
  }
};

export const signUp = async (formData: SignUp) => {
  try {
    const { data } = await api.post('/sign_up/', formData);
    return data;
  } catch (error) {
    if (axios.isAxiosError(error) && error.response?.data) {
      const serverErrors = error.response.data;

      const firstKey = Object.keys(serverErrors)[0];
      if (firstKey) {
        const errorData = serverErrors[firstKey];
        const message = Array.isArray(errorData) ? errorData[0] : errorData;

        if (firstKey.startsWith('password')) {
          throw new Error(message);
        }
        throw new Error(`${firstKey}: ${message}`);
      }
    }
    throw new Error('Registration failed');
  }
};

export const signOut = async () => {
  localStorage.removeItem('access_token');
  localStorage.removeItem('refresh_token');

  window.location.href = '/member/';
};

export const updateProfile = async (data: UpdateProfileRequest) => {
  try {
    const response = await api.patch('/profile/update/', data);
    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      throw new Error(error.response?.data?.detail || 'Update profile failed');
    }
    throw new Error('An unexpected error occurred');
  }
};

export const changePassword = async (data: ChangePasswordRequest) => {
  try {
    const response = await api.put('/profile/change_password/', data);
    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      const data = error.response?.data;
      if (data?.old_password) {
        throw new Error(data.old_password[0]);
      }
      throw new Error(data?.detail || 'The password is too simple.');
    }
    throw new Error('An unexpected error occurred');
  }
};