from django.contrib import admin

# Register your models here.
from .models import Choice, Question


#this is a default form representation of the Question class. However, if you want to customize how it works

#this is especially important when you have a LOT of fields, which requires a more intuitive order...
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        
        (None,      {'fields': ['question_text']}), 
        ('Date Information', {'fields': ['pub_date'], 'classes':
                              ['collapse']}),

    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']

    list_display = ('question_text', 'pub_date', 'was_published_recently')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)