from flask import Blueprint, render_template, request
from databases.models import Word
from sqlalchemy.sql.expression import func
from sqlalchemy import or_

just_one = Blueprint('random_word', __name__, )


@just_one.route('/justone', methods=['GET', 'POST'])
def get_word_from_db():
    # Default settings
    selected_difficulty = 'Adults'
    difficulties = [{'Kids': ''},
                    {'Adults': ''},
                    {'Extreme': ''}]
    difficulty_number = None  # This gets a value later

    if request.method == 'POST':
        selected_difficulty = request.form.getlist('difficulty_radio')[0]

    # Iterate through all difficulties. One will have value 'checked', others ''.
    # This is for HTML radio button.
    for i, difficulty in enumerate(difficulties):
        for key in difficulty.keys():
            if key == selected_difficulty:
                difficulty[key] = 'checked'
                difficulty_number = i
            else:
                difficulty[key] = ''

    if difficulty_number is not None:
        # Get a Just One compatible word from the corpus
        query_result = Word.query.filter(Word.difficulty <= difficulty_number) \
            .filter(or_(Word.is_subs, Word.is_name)) \
            .order_by(func.random()) \
            .limit(1).all()
        query_result = query_result[0].word
    else:
        query_result = 'Forbidden FORM POST. Does not match to keys in dictionary.'

    return render_template("justone.html", difficulties=difficulties, query_result=query_result)
