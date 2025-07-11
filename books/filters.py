import django_filters
from .models import Ebook, AudioFile

class EbookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    author = django_filters.CharFilter(field_name='author', lookup_expr='icontains')

    class Meta:
        model = Ebook
        fields = ['title', 'author']

class AudioFileFilter(django_filters.FilterSet):
    page = django_filters.CharFilter(field_name='page', lookup_expr='icontains')
    ebook_title = django_filters.CharFilter(field_name='ebook__title', lookup_expr='icontains')
    ebook_author = django_filters.CharFilter(field_name='ebook__author', lookup_expr='icontains')

    class Meta:
        model = AudioFile
        fields = ['page', 'ebook_title', 'ebook_author']

