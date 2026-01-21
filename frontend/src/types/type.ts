// Index
export interface Banner {
  id: number;
  image: string;
  caption?: string | null;
  is_active: boolean;
}

export interface NewsImage {
  id: number;
  image: string;
  caption?: string | null;
  order: number;
}

export interface News {
  id: number;
  title: string;
  contents_main: string;
  is_featured: boolean;
  created_at: string;
  updated_at: string;
  images: NewsImage[];
}

export interface NoticeImage {
  id: number;
  image: string;
  caption?: string | null;
  order: number;
}

export interface Notice {
  id: number;
  title: string;
  contents_main: string;
  subtitle_1: string;
  contents_1: string;
  subtitle_2: string;
  contents_2: string;
  lat: string;
  lng: string;
  address: string;
  map_id: string;
  is_featured: boolean;
  created_at: string;
  updated_at: string;
  images: NoticeImage[];
}

export interface Quote {
  id: number;
  author: string;
  content: string;
  is_active: boolean;
}

// Activity
export interface ActivityImage {
  id: number;
  image: string;
  caption?: string | null;
  order: number;
}

export interface Activity {
  id: number;
  type: 'hands_on' | 'performance' | 'exhibition' | 'lecture' | 'workshop';
  title: string;
  is_appointment: 'yes' | 'no';
  fee_details: string;
  currency: 'JPY' | 'USD' | 'EUR';
  minimum_charge: number;
  price_included: string;
  provider: string;
  participants: string;
  participating_age: string;
  duration: string;
  description: string;
  plan_1?: string | null;
  price_1?: string | null;
  summary_1?: string | null;
  plan_2?: string | null;
  price_2?: string | null;
  summary_2?: string | null;
  plan_3?: string | null;
  price_3?: string | null;
  summary_3?: string | null;
  min_p: string;
  reg_deadline: string;
  event_ends: string;
  prefecture:
  | 'hokkaido'
  | 'aomori' | 'iwate' | 'miyagi' | 'akita' | 'yamagata' | 'fukushima'
  | 'ibaraki' | 'tochigi' | 'gunma' | 'saitama' | 'chiba' | 'tokyo' | 'kanagawa'
  | 'niigata' | 'toyama' | 'ishikawa' | 'fukui' | 'yamanashi' | 'nagano' | 'gifu' | 'shizuoka' | 'aichi'
  | 'mie' | 'shiga' | 'kyoto' | 'osaka' | 'hyogo' | 'nara' | 'wakayama'
  | 'tottori' | 'shimane' | 'okayama' | 'hiroshima' | 'yamaguchi'
  | 'tokushima' | 'kagawa' | 'ehime' | 'kochi'
  | 'fukuoka' | 'saga' | 'nagasaki' | 'kumamoto' | 'oita' | 'miyazaki' | 'kagoshima' | 'okinawa';
  lat: string;
  lng: string;
  address: string;
  map_id: string;
  created_at: string;
  updated_at: string;
  images: ActivityImage[];
}

export interface Booking {
  id?: number;
  activity: string;
  first_name: string;
  last_name: string;
  email: string;
  phone?: string | null;
  prefer_date: string;
  comment?: string | null;
  created_at: string;
  activity_obj?: number | null;
  user?: number | null;
}

export interface ActivityListResponse {
  results: Activity[];
  count: number;
  next?: string | null;
  previous?: string | null;
}
