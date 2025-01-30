
export interface ParentCategory {
  slug: string,
}

export interface ArtistCategory {
  title: string,
  slug: string,
  parent: ParentCategory,
  permalink: string,
}

export enum ArtistPortfolioType {
  MUSIC = 'music',
  DRAWING = 'drawing',
  PHOTO = 'photo',
  VIDEO = 'video',
}

export interface ArtistPortfolio {
  id: Number,
  title: string,
  upload_type: ArtistPortfolioType,
  thumbnail: string|null,
  media: string|null,
}

export interface Artist {
  name: string,
  slug: string,
  title: string,
  photo: string|null,
  photo_thumbnail: string|null,
  categories: ArtistCategory[]|null,
  related: Artist[]|null,
  featured: Boolean,
  biography: string,
  birth_date: Date|null,
  birth_city: string|null,
  artistic_kinship: string|null,
  groups_affiliation: string|null,
  works: string|null,
  website: string|null,
  instagram: string|null,
  facebook: string|null,
  whatsapp: string|null,
  youtube: string|null,
  portfolio: ArtistPortfolio[],
  // custom attributes
  permalink: string,
  rank: Number,
  created_at: Date,
}

export interface Article {
  title: string,
  slug: string,
  image: string,
  image_thumbnail: string,
  created_at: Date,
}

export interface ApiError {
  message: string,
  code: string,
  status: Number,
  data: Object,
}

export enum ReadyStateType {
  LOADING = 'loading',
  SUCCESS = 'success',
  ERROR = 'error',
}
