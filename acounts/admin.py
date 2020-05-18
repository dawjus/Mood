from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = "Mood Admin"
admin.site.site_title = "Mood Admin Area"
admin.site.index_title = "Welcome to the Mood Admin Area"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}), ('Date Information', {
        'fields': ['question_category'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
