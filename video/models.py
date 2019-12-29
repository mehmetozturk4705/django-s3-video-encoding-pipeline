from django.db import models

# Create your models here.
class Video(models.Model):
    class Meta:
        db_table = 'dim_videos'
    video_key = models.CharField(max_length=500, null=False, unique=True)
    video_key_mp4_720p=models.CharField(max_length=500, null=True)
    video_key_mp4_480p = models.CharField(max_length=500, null=True)
    video_key_mp4_360p = models.CharField(max_length=500, null=True)
    video_key_webm_720p = models.CharField(max_length=500, null=True)
    video_key_webm_480p = models.CharField(max_length=500, null=True)
    video_key_webm_360p = models.CharField(max_length=500, null=True)
    video_length_seconds = models.PositiveIntegerField( null=True)
    video_encoded = models.BooleanField(db_index=True, null=True)
    video_encoding_date = models.DateTimeField(null=True)
    video_encoding_percentage=models.PositiveSmallIntegerField(null=True)