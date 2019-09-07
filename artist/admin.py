from django.contrib import admin

from .models import Job, JobCategory, Artist


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('category',)
    search_fields = ('name', 'category__name')


class JobInlineAdmin(admin.TabularInline):
    model = Job
    extra = 1
    prepopulated_fields = {'slug': ('name',)}


@admin.register(JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    inlines = (JobInlineAdmin,)


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'birth_date', 'age', 'created_at')
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
    search_fields = ('first_name', 'last_name', 'jobs__name')
