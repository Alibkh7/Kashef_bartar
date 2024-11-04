from django.contrib import admin
from .models import Service, Sample, SampleImage


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'body1', 'body2', 'image', 'image1', 'image2', 'created')
    search_fields = ('title',)


class SampleImageInline(admin.TabularInline):
    model = SampleImage
    extra = 1


@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'body', 'image', 'customer', 'date')
    inlines = [SampleImageInline]


@admin.register(SampleImage)
class SampleImageAdmin(admin.ModelAdmin):
    list_display = ('sample', 'image')