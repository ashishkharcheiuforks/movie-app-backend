from django.contrib import admin

from .models import Genre, Movie, Comment, Trailer, MovieArtist


class TrailerInlineAdmin(admin.TabularInline):
    model = Trailer
    extra = 1


class MovieArtistInlineAdmin(admin.TabularInline):
    model = MovieArtist
    extra = 1


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'rating', 'release_date', 'created_at')
    list_filter = ('country', 'movieartist__artist')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'movieartist__artist__first_name')
    inlines = ()

    def get_inline_instances(self, request, obj=None):
        self.inlines = (TrailerInlineAdmin, MovieArtistInlineAdmin) if obj else []
        return super().get_inline_instances(request, obj)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Trailer)
class TrailerAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'title', 'release_date', 'created_at')
    search_fields = ('title', 'movie__name')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'user', 'confirmed', 'created_at')
    list_filter = ('movie', 'user', 'confirmed', 'created_at')
    search_fields = ('comment', 'movie__name', 'user__username', 'user__first_name', 'user__last_name')

    def get_readonly_fields(self, request, obj=None):
        self.readonly_fields = ('movie', 'user') if obj else ()
        return super().get_readonly_fields(request, obj)
