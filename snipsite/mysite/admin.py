from mysite.models import Snippet, Category, Language
from django.contrib import admin

admin.site.register(Category)

class LanguageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}

class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'rating_score', 'pub_date')
    date_hierarchy = 'pub_date'
    

admin.site.register(Language, LanguageAdmin)
admin.site.register(Snippet, SnippetAdmin)

