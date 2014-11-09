import os
import csv
from glob import glob
from config import ANSWERS_DIR
from flask.ext.script import Command
from extensions import db
from models import Answer


class ParseAnswers(Command):
    """
    parses answers from file
    """

    def run(self):
        Answer.query.delete()
        db.session.commit()
        for file_name in glob(os.path.join(ANSWERS_DIR, '**/*.csv')):
            with open(file_name, 'rb') as csvfile:
                locale = file_name.split('/')[-2]
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    answer = Answer()
                    answer.locale = locale
                    answer.text = unicode(row[0], 'utf-8')
                    db.session.add(answer)
                db.session.commit()
