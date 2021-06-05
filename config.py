import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    FER_HOST = "http://192.168.1.154:8000"
    FER_IMAGE_URL = f'{FER_HOST}/image'
    FER_VIDEO_URL = f'{FER_HOST}/video'
