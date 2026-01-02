export interface Banner {
  id: number;
  caption: string;
  image: string;
  is_active: boolean;
}

export interface Quote {
  id: number;
  author: string;
  content: string;
  is_featured: boolean;
}
