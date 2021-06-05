import base64
from io import BytesIO

from flask import render_template, send_file
import requests

from config import Config
from . import main
from .forms import ImageForm, VideoForm


@main.route('/')
def hello_world():
    return render_template('home_page.html')


@main.route('/webcam')
def webcam():
    return render_template('webcam.html')


@main.route('/image', methods=['GET', 'POST'])
def image():
    form = ImageForm()
    context = {'form': form}
    if form.validate_on_submit():
        img = form.img.data.read()
        files = {'image': img}
        # response = requests.post(Config.FER_IMAGE_URL, files=files)
        # response.raise_for_status()
        # context['len_content'] = len(img)
        img_base64 = base64.b64encode(img).decode('utf-8')
        context['img_base64'] = img_base64
    return render_template('image.html', **context)


@main.route('/video', methods=['GET', 'POST'])
def video():
    form = VideoForm()
    context = {'form': form}
    if form.validate_on_submit():
        video_ = form.video.data.read()
        files = {'video': video_}
        response = requests.post(Config.FER_VIDEO_URL, files=files)
        response.raise_for_status()
        buffer = BytesIO()
        buffer.write(response.content)
        buffer.seek(0)
        return send_file(buffer, as_attachment=True, download_name='video.mp4')
    return render_template('video.html', **context)
