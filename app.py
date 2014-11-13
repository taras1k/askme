import os
from glob import glob
from random import choice
from flask import Flask, render_template, jsonify, request
from flask.ext.babel import gettext as _
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from extensions import db, babel
from models import Question, Answer
from commands import ParseAnswers

app = Flask(__name__)
app.config.from_object('config')
babel.init_app(app)
db.init_app(app)
db.app = app
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('parse_answers', ParseAnswers)


def _get_random_background():
    backgrounds_list = glob(os.path.join(
        app.config.get('BACKGROUND_IMAGES_DIRR'), '*.jpg'))
    background_path = choice(backgrounds_list)
    background_path = background_path.split('/')[-2:]
    return '/'.join(background_path)


@app.errorhandler(404)
def page_not_found(error):
    data = {'background_image': _get_random_background()}
    return render_template('404.html', **data), 404


@app.route('/')
def index():
    data = {'background_image': _get_random_background()}
    return render_template('index.html', **data)


@app.route('/post_question', methods=['POST'])
def post_answer():
    data = {}
    if request.form['question']:
        question = Question()
        question.text = request.form['question']
        db.session.add(question)
        db.session.commit()
        answer = Answer.query.all()
        if answer:
            answer = choice(answer)
            data['answer'] = answer.text
        return jsonify(data)
    else:
        data['error'] = _('question is missing')
        return jsonify(data), 400


if __name__ == '__main__':
    manager.run()
