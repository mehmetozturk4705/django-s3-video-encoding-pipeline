# Django S3 Video Encoding Pipeline
Django is a robust web framework with instant development capabilities. This repository demonstrates robust features of django, django rest framework and depicts how video pipeline should be.

Demonstration will continue with ffmpeg encoding integration.

    git clone https://github.com/mehmetozturk4705/django-s3-video-encoding-pipeline
    cd django-s3-video-encoding-pipeline
    python -m virtualenv venv
    #On Linux or Mac
    source venv/bin/activate
    #On Windows
    .\venv\Scripts\activate
    pip install -r requirements.txt
    
You should create a file named **.env** and add lines below

    AWS_ACCESS_KEY_ID=<AWS KEY>
    AWS_SECRET_ACCESS_KEY=<AWS SECRET>
    
and...
    
    python manage.py runserver