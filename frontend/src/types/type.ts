export interface Banner {
  id: number;
  image: string;
  caption: string;
  is_active: boolean;
}

export interface NewsImage {
  id: number;
  image: string;
  caption: string;
  order: number;
}

export interface News {
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

  main_image_url: string;
  images: NewsImage[];
}

export interface Quote {
  id: number;
  author: string;
  content: string;
  is_active: boolean;
}
