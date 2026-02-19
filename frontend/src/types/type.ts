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
  type_display: string;
  title: string;
  is_appointment: 'yes' | 'no';
  fee_details: string;
  currency: 'JPY' | 'USD' | 'EUR';
  minimum_charge: string;
  price_included: string;
  provider: string;
  participants: string;
  target_age: string;
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
  prefecture_display: string;
  lat: string;
  lng: string;
  address: string;
  map_id: string;
  created_at: string;
  updated_at: string;
  images: ActivityImage[];
}

export interface PrefectureOption {
  value: string;
  label: string;
}

export interface RegionGroup {
  label: string;
  prefectures: PrefectureOption[];
}

export interface Booking {
  id?: number;
  title: string;
  first_name: string;
  last_name: string;
  email: string;
  phone?: string | null;
  prefer_date: string;
  comment?: string | null;
  created_at: string;
  activity_id: number;
  activity_obj: Activity;
  user?: number | null;
}

// Collection
export interface CollectionImage {
  id: number;
  image: string;
  caption?: string | null;
  order: number;
}

export interface Collection {
  id: number;
  type: 'tachi' | 'katana' | 'kodachi' | 'wakizashi' | 'tanto';
  type_display: string;
  name_jp: string;
  name_en: string;
  provider: string;
  signature: string;
  currency: 'JPY' | 'USD' | 'EUR';
  price: number;
  blade_length: number;
  curvature: number;
  sword_weight: number;
  motohaba: number;
  sakihaba: number;
  motogasane: number;
  sakigasane: number;
  period_type: 'koto' | 'chūkoto' | 'shinto' | 'gendaito';
  period: string;
  koshirae: string;
  registration: string;
  certificate: string;
  remarks: string;
  created_at: string;
  updated_at: string;
  images: CollectionImage[];
}

export interface Order {
  id?: number;
  name_jp: string;
  first_name: string;
  last_name: string;
  email: string;
  phone?: string | null;
  payment: string;
  address: string;
  comment?: string | null;
  created_at: string;
  collection_id: number;
  collection_obj: Collection;
  user?: number | null;
}

// Filters
export interface FilterOption<T> {
  value: T;
  label: string;
}

export interface ActivityFilterOptions {
  types: FilterOption<Activity['type']>[];
  price: FilterOption<Activity['minimum_charge']>[];
  until: FilterOption<Activity['event_ends']>[];
  region_groups: RegionGroup[];
}

export interface ActivityFilterState {
  q: string;
  types: string[];
  charge_min: string;
  charge_max: string;
  event_ends: string;
  prefectures: string[];
  page: number;
}

export interface CollectionFilterOptions {
  types: FilterOption<Collection['type']>[];
  price: FilterOption<Collection['price']>[];
  period_types: FilterOption<Collection['period']>[];
  blade_length: FilterOption<Collection['blade_length']>[];
}

export interface CollectionFilterState {
  q: string;
  types: string[];
  price_min: string;
  price_max: string;
  period_types: string[];
  length_min: string;
  length_max: string;
  page: number;
}

// Pagination
export interface PaginatedResponse<T> {
  count: number;
  next: string | null;
  previous: string | null;
  results: T[];
}

// Kenshi
export interface Kenshi {
  id: number;
  title: string;
  content: string;
  image: string;
  video: string;
  created_at: string;
  updated_at: string;
}

// Member
export interface MemberProfile {
  id: number;
  username: string;
  first_name: string;
  last_name: string;
  email: string;
  phone: string;
  payment: string;
  address: string;
  bookings: Booking[];
  orders: Order[];
}

export interface SignIn {
  username: string;
  password: string;
}

export interface SignUp {
  username: string;
  email: string;
  password1: string;
  password2: string;
}

export interface AuthResponse {
  access: string;
  refresh: string;
}

export interface RegisterResponse {
  id: number;
  username: string;
  email: string;
}

export interface UpdateProfileRequest {
  first_name?: string;
  last_name?: string;
  email?: string;
  phone?: string;
  payment?: string;
  address?: string;
}

export interface ChangePasswordRequest {
  old_password: string;
  new_password: string;
  confirm_password: string;
}