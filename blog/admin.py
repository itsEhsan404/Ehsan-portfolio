from django.contrib import admin

from .models import post


@admin.register(post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'category', 'created_at'
    )
    
    
    list_filter = (
        'category', 'created_at'
    )
    
    
    search_fields = (
        'title', 'content'
    )
    
    
    ordering = (
        '-created_at',
    )