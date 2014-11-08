import os
from glob import glob
from random import choice
from flask import Flask, render_template
from extensions import db, babel


app = Flask(__name__)
app.config.from_object('config')
babel.init_app(app)
db.init_app(app)
db.app = app


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route('/')
def index():
    data = {}
    backgrounds_list = glob(os.path.join(
        app.config.get('BACKGROUND_IMAGES_DIRR'), '*.jpg'))
    background_path = choice(backgrounds_list)
    background_path = background_path.split('/')[-2:]
    data['background_image'] = '/'.join(background_path)
    return render_template('index.html', **data)

if __name__ == '__main__':
    app.run()
