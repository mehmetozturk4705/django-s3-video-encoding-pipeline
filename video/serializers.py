from rest_framework import serializers
from rest_framework.exceptions import *
from django.conf import settings
from .models import Video

class VideoPutSerializer(serializers.Serializer):
    filename = serializers.CharField()
    def validate_filename(self, p_filename):
        filename_sp = p_filename.split('.')
        if len(filename_sp)<2:
            raise ValidationError('Not a valid filename. You should define extension.')
        if filename_sp[-1] not in settings.VIDEO_ALLOWED_EXTENSIONS:
            raise ValidationError(
                f'Not a valid file type. Allowed one of these : {".".join(settings.VIDEO_ALLOWED_EXTENSIONS)}')
        return p_filename

class VideoPostSerializer(serializers.Serializer):
    video_key = serializers.CharField()
    def validate_video_key(self, video_key):
        try:
            video_obj = Video.objects.get(video_key=video_key, video_encoding_percentage=None)
        except Video.DoesNotExist as e:
            raise ValidationError('No uploaded video with provided key.')
        return video_obj