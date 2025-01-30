from django.http import Http404
from django.db.models import Q

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics

from artists.models import Artist, Category
from news.models import Article
from .serializers import ArtistSerializer, ArtistListSerializer, CategorySerializer, ArticleSerializer
from .helpers import MultiSerializerReadOnlyViewSet

class ArtistViewSet(MultiSerializerReadOnlyViewSet):
    serializers = { 
        'default': ArtistListSerializer,
        'list': ArtistListSerializer,
        'retrieve': ArtistSerializer,
    }
    lookup_field = 'slug'

    def get_queryset(self):
        """
        Optionally restricts the returned artists to a given category,
        """
        queryset = Artist.objects.order_by('-featured', '-views', '-created_at')
        category = self.request.query_params.get('category')
        if category is not None:
            queryset = queryset.filter(Q(categories__slug=category) | Q(categories__parent__slug=category))
        queryset = queryset.prefetch_related('categories', 'categories__parent')
        return queryset

    def get_object(self):
        """
        Lookup slug and past_slugs for a given object.
        """
        queryset = self.filter_queryset(self.get_queryset())

        # lookup current slug or past slugs
        try:
          obj = generics.get_object_or_404(queryset, slug=self.kwargs['slug'])
        except (Http404):
          obj = generics.get_object_or_404(queryset, past_slugs__contains=self.kwargs['slug'])
          
        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        # artist view count
        obj.increment_views()

        return obj

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return (Category.objects
            .prefetch_related('parent')
            .order_by('-featured', 'created_at'))

class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.filter(featured=True).order_by('-created_at')

