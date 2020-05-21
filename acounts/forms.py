from django import forms
import json


def get_questions():
    with open('project/questions.json') as f:
        file_questions = json.load(f)

    questions = []
    for question in file_questions:
        questions.append(question['fields']['question_text'])

    return questions


def get_choices(question_sum):
    with open('project/choices.json') as f:
        file_choices = json.load(f)

    choices = []
    for question_number in range(1, question_sum + 1):
        filtered_choices = filter(
            lambda choice: choice['fields']['question'] == question_number, file_choices)

        cleaned_choices = []
        for choice in filtered_choices:
            choice_text = choice['fields']['choice_text']
            cleaned_choices.append((choice_text, choice_text))

        choices.append(cleaned_choices)

    return choices


class GetMoviePreferences(forms.Form):
    questions = get_questions()
    choices = get_choices(len(questions))

    mood = forms.ChoiceField(choices=choices[0], label=questions[0])
    genre = forms.ChoiceField(choices=choices[1], label=questions[1])
    will_lead_to_reflect = forms.ChoiceField(
        choices=choices[2], label=questions[2])
    lead_to_think = forms.ChoiceField(choices=choices[3], label=questions[3])
    kind = forms.ChoiceField(choices=choices[4], label=questions[4])
