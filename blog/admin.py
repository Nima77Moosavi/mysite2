from django.contrib import admin
from .models import Post, Category

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    ordering = ['title']
    date_hierarchy = 'published_date'
    empty_value_display = '-empty-'
    list_display = ['title', 'author', 'counted_views', 'status', 'published_date', 'created_date']
    list_filter = ['status', 'author']

admin.site.register(Post, PostAdmin)
admin.site.register(Category)