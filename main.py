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
@app.route('/<name>')
def index(name=None):
    return Template('index').render(name=name)


@lru_cache()
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
