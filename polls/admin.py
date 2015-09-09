from django.contrib import admin

from .models import Question, Choice

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ] # This is for admin items with dozons of fields
    inlines = [ChoiceInline]
    # This tells Django: "Choice objects are edited on the Question admin page.
    # By default, provide enough fields for 3 choices.
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    # uses LIKE query behind the scenes, limiting the number of search fields to a reasonable number will make it easier for your database to do the search.



admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)