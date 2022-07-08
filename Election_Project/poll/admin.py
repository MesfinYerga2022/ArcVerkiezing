from django.contrib import admin
from .models import Poll,Choice
#from .views import create
# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date','close_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date','close_date')
    list_display = ('question', 'pub_date','close_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Poll,QuestionAdmin)
admin.site.register(Choice)
#admin.site.register(create)
