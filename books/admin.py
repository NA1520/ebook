from django.contrib import admin
from .models import Ebook, AudioFile

class AudioInline(admin.TabularInline):
    model = AudioFile
    extra = 1

@admin.register(Ebook)
class EbookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year', 'grade', 'who', 'slug')
    search_fields = ('title', 'author')
    list_filter = ('year', 'who')
    inlines = [AudioInline]

@admin.register(AudioFile)
class AudioFileAdmin(admin.ModelAdmin):
    list_display = ('ebook', 'page', 'audio_mark', 'order', 'audio_file', 'audio_type', 'description')
    list_filter = ('ebook', 'page', 'audio_type')
    search_fields = ('ebook__title', 'audio_mark', 'description')
