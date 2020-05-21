from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
import json
from project.filtermovie import filtermovie
from .forms import GetMoviePreferences


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def get_all_questions(request):

    form = GetMoviePreferences()
    context = {
        'form': form,
    }

    return render(request, 'questions.html', context)


def get_results(request):

    if request.method == 'POST':

        form = GetMoviePreferences(request.POST)
        result = {
            'mood': request.POST['mood'],
            'genre': request.POST['genre'],
            'will_lead_to_reflect': request.POST['will_lead_to_reflect'],
            'lead_to_think': request.POST['lead_to_think'],
            'kind': request.POST['kind'],
        }

        movies = filtermovie(
            result['genre'], result['mood'], result['will_lead_to_reflect'], result['lead_to_think'], result['kind'])

        context = {
            'sentiment': movies
        }
        return render(request, 'results.html', context)
