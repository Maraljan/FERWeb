from flask import render_template

from . import main
from .forms import ImageForm, VideoForm


@main.route('/')
def hello_world():
    return render_template('home_page.html')


@main.route('/webcam')
def webcam():
    return render_template('webcam.html')


@main.route('/image')
def image():
    form = ImageForm()
    return render_template('image.html', form=form)


@main.route('/video')
def video():
    form = VideoForm()
    return render_template('video.html', form=form)
