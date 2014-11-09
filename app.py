import os
from glob import glob
from random import choice
from flask import Flask, render_template, jsonify, request
from flask.ext.babel import gettext as _
from extensions import db, babel, admin
from models import Question, Answer
from flask.ext.admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config.from_object('config')
babel.init_app(app)
db.init_app(app)
admin.init_app(app)
db.app = app


#model admin
admin.add_view(ModelView(Question, db.session))
admin.add_view(ModelView(Answer, db.session))


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
    app.run()
