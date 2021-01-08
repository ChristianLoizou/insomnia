#!/usr/bin/env python3
import os
from datetime import datetime
from functools import lru_cache

import pytz
from astral import LocationInfo
from astral.sun import sun
from flask import Flask, render_template


class Template:
    def __init__(self, name, style=None, extension="jinja"):
        self.name = name
        self.path = f"html/{self.name}.{extension}"
        self.style = self.get_stylsheet(style)

    def get_stylsheet(self, style):
        if style is None:
            return load_css(f"{self.name}.css")
        else:
            return load_css(style)

    def render(self, **kwargs):
        return render_template(self.path, _style=self.style, **kwargs)


app = Flask(__name__)


@app.route('/')
def index():
    current_time, logo_scheme = get_logo_colour_scheme()
    formatted_time = current_time.strftime("%H:%M\t%A, %b %-d")
    return Template('index').render(
        date_time=formatted_time,
        logo_bubble_back=logo_scheme["bubble_back"],
        mountain_back=logo_scheme["mountain_back"],
        projects=projects
    )


@app.route('/p5js/sketch')
def chess():
    return Template('p5js_sketch').render()


# lru_cache will cache .css files, so if one file is used twice the script doesn't have to load it twice
@lru_cache(maxsize=None)
def load_css(stylesheet_name):
    return css[stylesheet_name]


def load_stylesheets(path="styles/"):
    css = dict()
    for file_name in os.listdir(path):
        with open(f"{path}/{file_name}", 'r') as stylesheet:
            css[file_name] = stylesheet.read()
    return css


def get_logo_colour_scheme(override=None):
    schemes = {
        "day": {
            "bubble_back": "#C1F1FF",
            "mountain_back": "#2E5F55"
        },
        "night": {
            "bubble_back": "#333388",
            "mountain_back": "#eeeeee"
        }
    }
    utc = pytz.UTC
    current_time = datetime.now(utc)
    if override is not None:
        return current_time, schemes[override]
    london = LocationInfo("London", "England", "Europe/London", 51.5, -0.116)
    s = sun(london.observer, date=current_time)
    if s["dawn"] < current_time <= s["dusk"]:
        return current_time, schemes["day"]
    else:
        return current_time, schemes["night"]


if __name__ == "__main__":
    css = load_stylesheets()
    projects = {
        "P5.js Sketch": '/p5js/sketch'
    }
    app.run(debug=True)
