from flask import render_template

from . import main
from .forms import ImageForm


@main.route('/')
def hello_world():
    return render_template('home_page.html')


@main.route('/video')
def video():
    return render_template('video.html')


@main.route('/webcam')
def webcam():
    return render_template('webcam.html')


@main.route('/image')
def image():
    form = ImageForm()
    return render_template('image.html', form=form)

