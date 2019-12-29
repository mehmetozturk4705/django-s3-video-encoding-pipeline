from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import VideoPostSerializer, VideoPutSerializer
from django.db import transaction
from .models import Video
from django.conf import settings
import mimetypes
from Tutorial.aws_bean import S3Client
import uuid

# Create your views here.
class VideoView(APIView):
    def get(self, request):
        success_token = request.query_params.get("success")
        if success_token == "true":
            return Response({"detail": "Upload was successful"}, status.HTTP_200_OK)
        else:
            return Response({"detail": "Method not allowed"}, status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        serializer = VideoPostSerializer(data=request.data)
        if serializer.is_valid():
            video_obj = serializer.validated_data['video_key']
            video_obj.video_encoding_percentage = 0
            with transaction.atomic():
                video_obj.save()
                transaction.on_commit(lambda: print('ok')) ##Burada encoding queue ile video işlenmeli
                return Response({"detail": "Video is pushed into encoding queue."})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        """
        Checking if input filename is true
        """
        serializer = VideoPutSerializer(data=request.data)
        if serializer.is_valid():
            #Creating video object
            filename = serializer.validated_data.get('filename')
            extension = filename.split(".")[-1]
            with transaction.atomic():
                video_obj = Video(video_encoded=False)
                video_obj.save()

            #Creating upload key
            upload_key = f"media/video/{video_obj.id}-{uuid.uuid4().hex}/{video_obj.id}.{extension.lower()}"
            with transaction.atomic():
                video_obj.video_key=upload_key
                video_obj.save()

            mimetype = mimetypes.MimeTypes().guess_type(filename)[0]

            url = S3Client.getInstance().generate_presigned_post(
                Bucket=settings.AWS_STORAGE_BUCKET_NAME,
                Key=upload_key,
                Fields={
                    "acl": "public-read",
                    "bucket": settings.AWS_STORAGE_BUCKET_NAME,
                    "success_action_redirect": request.get_host() + "/api/views/video/?success=true",
                    "content-type": mimetype
                },
                Conditions=[
                    {"acl": "public-read"},
                    ["starts-with", "$content-type", "video/"],
                    {"bucket": settings.AWS_STORAGE_BUCKET_NAME},
                    {"success_action_redirect": request.get_host() + "/api/views/video/?success=true"},
                    ["content-length-range", 0, settings.VIDEO_MAX_FILE_SIZE]
                ],
                ExpiresIn=settings.VIDEO_ALLOWED_UPLOAD_MARGIN
            )
            #TODO: Remove before production
            for key in url['fields']:
                print(f"{key}:{url['fields'][key]}")
            return Response(url)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)