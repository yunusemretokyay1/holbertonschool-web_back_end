#!/usr/bin/env python3
"""i18n """
from flask_babel import Babel, _
from flask import Flask, render_template, request, flash

app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config(object):
    """Config for languages """

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    """Return index"""
    return render_template("4-index.html")


@babel.localeselector
def get_locale() -> str:
    """Get locale selector for babel"""
    if request.args.get('locale'):
        return request.args.get('locale')
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
