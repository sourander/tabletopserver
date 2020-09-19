from databases.shared import db


class Word(db.Model):
    __tablename__ = 'words'

    word_id = db.Column('id', db.Integer, primary_key=True, nullable=False)
    word = db.Column(db.String(18), nullable=False)
    is_verb = db.Column(db.Boolean, nullable=False)
    is_subs = db.Column(db.Boolean, nullable=False)
    is_adje = db.Column(db.Boolean, nullable=False)
    is_nume = db.Column(db.Boolean, nullable=False)
    is_name = db.Column(db.Boolean, nullable=False)
    difficulty = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, word_id, word, is_verb, is_subs, is_adje, is_nume, is_name, difficulty):
        self.word_id = word_id
        self.word = word
        self.is_verb = is_verb
        self.is_subs = is_subs
        self.is_adje = is_adje
        self.is_nume = is_nume
        self.is_name = is_name
        self.difficulty = difficulty

    def __repr__(self):
        return f'Word: {self.word}'
