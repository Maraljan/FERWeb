import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    FER_HOST = "http://192.168.0.105:8001"
    FER_IMAGE_URL = f'{FER_HOST}/image'
    FER_VIDEO_URL = f'{FER_HOST}/video'
