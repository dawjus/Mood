from django.shortcuts import render
from django.http.request import HttpRequest
from django.http import HttpResponseNotAllowed, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from modules.movierating.public.MovieWithRating import MovieWithRating
from project.components.ratingList.MovieRatingMapper import from_string_to_enum
from project.services import MOVIE_STORAGE_SERVICE

from modules.movierating.public.MovieRating import MovieRating

@csrf_exempt
def movie_list(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()

    http_method = request.method
    if http_method == 'GET':
        return _method_get(request)

    return HttpResponseNotAllowed()

def _method_get(request):
    return render( request, 'movieList.html', {'movie_collection': MOVIE_STORAGE_SERVICE.get_all()})