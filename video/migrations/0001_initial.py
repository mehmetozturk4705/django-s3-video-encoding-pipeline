# Generated by Django 3.0.1 on 2019-12-29 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_key', models.CharField(max_length=500, unique=True)),
                ('video_key_mp4_720p', models.CharField(max_length=500, null=True)),
                ('video_key_mp4_480p', models.CharField(max_length=500, null=True)),
                ('video_key_mp4_360p', models.CharField(max_length=500, null=True)),
                ('video_key_webm_720p', models.CharField(max_length=500, null=True)),
                ('video_key_webm_480p', models.CharField(max_length=500, null=True)),
                ('video_key_webm_360p', models.CharField(max_length=500, null=True)),
                ('video_length_seconds', models.PositiveIntegerField(null=True)),
                ('video_encoded', models.BooleanField(db_index=True, null=True)),
                ('video_encoding_date', models.DateTimeField(null=True)),
                ('video_encoding_percentage', models.PositiveSmallIntegerField(null=True)),
            ],
            options={
                'db_table': 'dim_videos',
            },
        ),
    ]
