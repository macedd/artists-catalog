
export interface ArtistCategory {
  title: String,
  slug: String,
  // parent:
}

enum ArtistPortfolioType {
  MUSIC = 'music',
  DRAWING = 'drawing',
  PHOTO = 'photo',
  VIDEO = 'video',
}

export interface ArtistPortfolio {
  id: Number,
  title: String,
  upload_type: ArtistPortfolioType,
  link: String|null,
  upload: String|null,
}

export interface Artist {
  name: String,
  slug: String,
  photo: String|null,
  categories: ArtistCategory[]|null,
  related: Artist[]|null,
  featured: Boolean,
  biography: String,
  birth_date: Date|null,
  birth_city: String|null,
  artistic_kinship: String|null,
  groups_affiliation: String|null,
  works: String|null,
  website: String|null,
  instagram: String|null,
  facebook: String|null,
  whatsapp: String|null,
  portfolio: ArtistPortfolio[],
}

export interface Article {
  title: String,
  slug: String,
  image: String,
  created_at: Date,
}

export interface ApiError {
  message: String,
  code: String,
  status: Number,
  data: Object,
}