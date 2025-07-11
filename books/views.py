from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Ebook, AudioFile
from .serializers import EbookSerializer, AudioFileSerializer
from .filters import EbookFilter, AudioFileFilter

class EbookViewSet(viewsets.ModelViewSet):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EbookFilter

class AudioFileViewSet(viewsets.ModelViewSet):
    queryset = AudioFile.objects.all()
    serializer_class = AudioFileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AudioFileFilter

