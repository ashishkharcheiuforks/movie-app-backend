from django.contrib import admin

from .models import Genre, Movie, Comment


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'release_date', 'country', 'created_at')
    list_filter = ('country',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'user', 'confirmed', 'created_at')
    list_filter = ('movie', 'user', 'confirmed', 'created_at')
    search_fields = ('comment', 'movie__name', 'user__username', 'user__first_name', 'user__last_name')
