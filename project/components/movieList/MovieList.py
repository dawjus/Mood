from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.http import HttpResponseNotAllowed, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from modules.movierating.public.MovieWithRating import MovieWithRating
from project.components.ratingList.MovieRatingMapper import from_string_to_enum
from project.services import MOVIE_STORAGE_SERVICE, MOVIE_RATING_SERVICE

from modules.movierating.public.MovieRating import MovieRating

@csrf_exempt
def movie_list(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()

    http_method = request.method
    if http_method == 'GET':
        return _method_get(request)
    if http_method == 'POST':
        return _method_post(request)
    return HttpResponseNotAllowed()

def _method_post(request):
    user_id = request.user.id
    movie_id = int(request.POST.get('movie_id'))
    if user_id and movie_id:
        MOVIE_RATING_SERVICE.add_movie_to_rating(user_id, movie_id)
        return redirect("rating_list")
    return _method_get(request)

def _method_get(request):
    return render( request, 'movieList.html', {'movie_collection': MOVIE_STORAGE_SERVICE.get_all()})