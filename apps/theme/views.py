from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from django.views import generic

from .library import content_title
# Create your views here.

# homepage placeholder
def homepage(request):
    return render(request, 'home/placeholder.html')

# vuejs application
def vuejs(request, resource):
    # match content resource for rendering html metadata
    title = content_title(request.build_absolute_uri())
    return render(request, 'home/vuejs.html', {'title': title})



# class IndexView(generic.ListView):
#     template_name = 'artists/index.html'
#     context_object_name = 'latest_artists_list'

#     def get_queryset(self):
#         return Artist.objects.order_by('-created_at')[:5]

# class DetailView(generic.DetailView):
#     model = Artist
#     template_name = 'artists/detail.html'
#     slug_url_kwarg = 'artist_slug'
    
# def detail_canonical(request, artist_id):
#     try:
#         artist = Artist.objects.get(id=artist_id)
#     except Artist.DoesNotExist:
#         raise Http404("Artist does not exist")
            
#     return redirect('artists:detail', artist_slug=artist.slug)


# def index(request):
#     latest_artists_list = Artist.objects.order_by('-created_at')[:5]

#     context = {
#         'latest_artists_list': latest_artists_list,
#     }
#     return render(request, 'artists/index.html', context)

