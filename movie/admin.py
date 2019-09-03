from django.contrib import admin

from .models import Genre, Movie, Comment, Trailer


class TrailerInlineAdmin(admin.TabularInline):
    model = Trailer
    extra = 1


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Trailer)
class TrailerAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'title', 'release_date', 'created_at')
    search_fields = ('title', 'movie__name')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'rating', 'release_date', 'created_at')
    list_filter = ('country',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

    def get_inline_instances(self, request, obj=None):
        if obj:
            self.inlines = (TrailerInlineAdmin,)
        return super().get_inline_instances(request, obj)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'user', 'confirmed', 'created_at')
    list_filter = ('movie', 'user', 'confirmed', 'created_at')
    search_fields = ('comment', 'movie__name', 'user__username', 'user__first_name', 'user__last_name')
