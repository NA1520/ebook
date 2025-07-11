from rest_framework import serializers
from .models import Ebook, AudioFile

class AudioFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioFile
        fields = '__all__'

class EbookSerializer(serializers.ModelSerializer):
    audio_files = AudioFileSerializer(many=True, read_only=True, source='audiofile_set')

    class Meta:
        model = Ebook
        fields = '__all__'
