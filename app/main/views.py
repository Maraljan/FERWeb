from typing import TypedDict
import base64
import json
from io import BytesIO

import plotly.utils
from flask import render_template, send_file
import requests
import plotly.express as px
import pandas as pd

from config import Config
from . import main
from .forms import ImageForm, VideoForm


class Emotions(TypedDict):
    face_idx: int
    emotions_state: dict


@main.route('/')
def home_page():
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
        response = requests.post(Config.FER_IMAGE_URL, files=files)
        response.raise_for_status()
        context['len_content'] = len(img)
        img_base64 = base64.b64encode(response.content).decode('utf-8')
        context['img_base64'] = img_base64

        emotions: list[Emotions] = json.loads(response.headers['Emotions'])['emotions']
        figures = []
        for emotion in emotions:
            df = pd.DataFrame(dict(
                r=list(emotion['emotions_state'].values()),
                theta=list(emotion['emotions_state'].keys()),
            ))
            fig = px.line_polar(
                df,
                r='r',
                theta='theta',
                line_close=True,
                height=500,
                width=500,
                range_r=(0, 100),
            )
            # fig.update_traces(fill='toself')
            figures.append(fig)
        radars = []
        for fig, emotion in zip(figures, emotions):
            radars.append({
                'fig': json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder),
                'face_idx': emotion['face_idx'],
            })
        context['radars'] = radars

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
