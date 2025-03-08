from django.contrib import admin
from django import forms
from .models import Category, Post, Headding


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'parent', 'slug')
    search_fields = ('name', 'title', 'description', 'slug')
    prepopulated_fields = {'slug':('name',)}
    list_filter = ('parent', )
    ordering= ('name', )
    readonly_fields=('id', )


class HeadingInline(admin.TabularInline):
    model = Headding
    extra = 1
    fields = ('title', 'level', 'order','slug')
    prepopulated_fields = {'slug':('title',)}
    ordering = ('order',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'category', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'content', 'keywords', 'slug')
    prepopulated_fields = {'slug':('title',)}
    list_filter = ('status', 'category', 'updated_at',)
    ordering= ('-created_at', )
    readonly_fields=('id', 'created_at', 'updated_at', 'views')
    fieldsets = (
        ('General Information', {
            'fields':('title', 'description', 'content', 'thumbnail', 'keywords', 'slug', 'category')
        }),
        ('Status & Dates', {
            'fields':('status', 'created_at', 'updated_at')
        }),
    )
    inlines = [HeadingInline]

# @admin.register(Headding)
# class PostHeadding(admin.ModelAdmin):
#     list_display = ('title', 'post', 'level', 'order')
#     search_fields = ('title', 'post__title')
#     list_filter = ('level', 'post',)
#     ordering= ('post', 'order', )
#     prepopulated_fields = {'slug':('title',)}