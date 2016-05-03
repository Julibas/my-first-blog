from django.contrib import admin

from .models import Choice, Question


# Register your models here.
#admin.site.register(Question)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_feilds = ['question_text']
admin.site.register(Question, QuestionAdmin)

