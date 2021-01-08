#!/usr/bin/env python3
import os
from functools import lru_cache

from flask import Flask, render_template


class Template:
    def __init__(self, name, style=None):
        self.name = name
        self.path = f"html/{self.name}.jinja"
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
    return Template('index').render()


@lru_cache()  # this line caches .css files, so if one file is used twice the script doesn't have to load it twice
def load_css(stylesheet_name):
    return css[stylesheet_name]


def load_stylesheets(path="styles/"):
    css = dict()
    for file_name in os.listdir(path):
        with open(f"{path}/{file_name}", 'r') as stylesheet:
            css[file_name] = stylesheet.read()
    return css


if __name__ == "__main__":
    css = load_stylesheets()
    app.run(debug=True)
