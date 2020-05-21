from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
import json
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

        overall_sentiment = get_sentiment(result)

        context = {
            'sentiment': overall_sentiment
        }
        return render(request, 'results.html', context)


def get_sentiment(value):
    with open('project/choices.json') as f:
        file_choices = json.load(f)

    sentiment = 0
    for question_number in range(1, len(value) + 1):
        choice = list(filter(
            lambda choice: choice['fields']['question'] == question_number, file_choices))
        sentiment += choice[0]['fields']['coefficient']

    return sentiment / len(value)
