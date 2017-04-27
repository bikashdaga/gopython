from django.contrib import admin

# Register your models here.

from .models import Question
from .models import Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question infor', {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    # fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)