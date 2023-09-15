from urllib.parse import urlparse
from django.urls import path, get_resolver
from django.urls.resolvers import RegexPattern, URLResolver
from django.urls.exceptions import Resolver404

from artists.models import Artist

# routes from vuejs application (without leading slash /)
routes = [
    path('', str, name='placeholder'),
    path('home/', str, name='home'),
    path('a/<slug:artist>/', str, name='artist'),
]

def match_route(url):
    url_path = urlparse(url).path
    resolver = URLResolver(RegexPattern(r"^/"), routes)
    try:
        return resolver.resolve(url_path)
    except Resolver404:
        pass


def content_title(url):
    content = match_route(url)
    if not content:
        return None

    if content.url_name == 'artist':
        try:
            artist = Artist.get(content.kwargs.get('artist'))
        except Artist.DoesNotExist:
            return None
        return f"{artist.name}, {artist.title} - ArtejucanA"
    else:
        return None
