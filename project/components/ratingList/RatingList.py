from django.shortcuts import render
from django.http.request import HttpRequest
from django.http import HttpResponseNotAllowed, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from modules.movierating.public.MovieWithRating import MovieWithRating
from project.components.ratingList.MovieRatingMapper import from_string_to_enum
from project.services import MOVIE_RATING_SERVICE, MOVIE_STORAGE_SERVICE

from modules.movierating.public.MovieRating import MovieRating

MOVIE_RATING_SERVICE.add_movie_to_rating(5, 1)

@csrf_exempt
def rating_list(request):
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
    movie_rating = request.POST.get('movie_rating')

    rating = from_string_to_enum(movie_rating)

    rated_movie = MovieWithRating( user_id, movie_id, rating)

    MOVIE_RATING_SERVICE.rated_by_user(rated_movie)

    return _method_get(request)


def _method_get(request):
    user_id = request.user.id
    rated_movie_list = []
    waiting_for_rated_list = []

    for rated_movie in MOVIE_RATING_SERVICE.get_all_of_user(user_id):
        if rated_movie.get_rating() == MovieRating.WAITING_FOR_RATING:
            waiting_for_rated_list.append(rated_movie)
        else:
            rated_movie_list.append(rated_movie)

    print(len(rated_movie_list))
    print(len(waiting_for_rated_list))
    return render(request, 'RatingList.html', {'rated_movie_list': rated_movie_list,
                                                'rated_movie_list_empty': len(rated_movie_list) == 0,
                                                'waiting_for_rated_list': waiting_for_rated_list,
                                                'waiting_for_rated_list_empty': len(waiting_for_rated_list) == 0})




