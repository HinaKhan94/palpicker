from django.contrib import admin
from .models import Post, Request
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('description')
    actions = ['approve_posts']

    def approve_posts(self, request, queryset):
        queryset.update(approved=True)

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = (
        'post', 'first_name', 'message', 'status', 'approved'
    )
    search_fields = ['post', 'date_created', 'message']
    list_filter = ('status', 'date_created')
    actions = ['approve_requests']

    def approve_requests(self, request, queryset):
        queryset.update(approved=True)

