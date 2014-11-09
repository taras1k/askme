from extensions import db


class Question(db.Model):
    """
    Model for Questions
    """
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    created = db.Column(db.DateTime, default=db.func.now())
    updated = db.Column(db.DateTime, default=db.func.now(),
                           onupdate=db.func.now())


class Answer(db.Model):
    """
    Model for Answer
    """
    __tablename__ = 'answers'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    locale = db.Column(db.String(4))
    created = db.Column(db.DateTime, default=db.func.now())
    updated = db.Column(db.DateTime, default=db.func.now(),
                           onupdate=db.func.now())
