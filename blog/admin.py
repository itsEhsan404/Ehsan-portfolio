from django.contrib import admin
from .models import post


@admin.register(post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = (
        'title', 'slug', 'created_date', 'updated_date'
    )
    
    
    list_filter = (
        'category', 'created_date', 'updated_date'
    )
    
    
    search_fields = (
        'title', 'content'
    )
    
    
    ordering = (
        '-created_date',
    )