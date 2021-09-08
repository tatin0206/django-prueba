from django.contrib import admin
from .models import Question, Choice

# Register your models here.

#modificar el formulario de admin
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]

    list_display = ('question_text', 'pub_date', 'was_published_recently')
    #agregar una columna a la derecha para filtrar
    list_filter = ['pub_date']
    #agregar un campo de busqueda en admin
    search_fields = ['question_text']
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)