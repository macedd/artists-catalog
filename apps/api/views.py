from django.http import Http404

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
    queryset = Artist.objects.all().order_by('-created_at')
    lookup_field = 'slug'

    def get_queryset(self):
        """
        Optionally restricts the returned artists to a given category,
        """
        queryset = Artist.objects.all().order_by('-created_at')
        category = self.request.query_params.get('category')
        if category is not None:
            queryset = queryset.filter(categories__slug=category)
        return queryset

    def get_object(self):
        """
        Lookup slug and past_slugs for a given object.
        """
        queryset = self.filter_queryset(self.get_queryset())

        try:
          obj = generics.get_object_or_404(queryset, slug=self.kwargs['slug'])
        except (Http404):
          obj = generics.get_object_or_404(queryset, past_slugs__contains=self.kwargs['slug'])
          
        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all().order_by('parent')
    serializer_class = CategorySerializer
    lookup_field = 'slug'

class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.filter(featured=True).order_by('-created_at')

