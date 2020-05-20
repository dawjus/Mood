from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
import json


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def get_all_questions(request):
    with open('project/questions.json') as questions:
        all_questions = json.load(questions)
    with open('project/choices.json') as choices:
        all_choices = json.load(choices)
    choices_mapped = []
    for i in range(len(all_questions)):
        one_choice = list(filter(lambda x: x['fields']['question'] ==
                                 i+1, all_choices))
        choices_mapped.append(one_choice)

    context = {'questions': all_questions, 'choices': choices_mapped}
    return render(request, 'questions.html', context)


def get_results(request):
    context = {'message': 'RESULTS'}
    return render(request, 'results.html', context)
