from flask import Blueprint, render_template, request, session
from databases.models import Word
from databases.shared import db
from games.justone.helpers import update_difficulty
from sqlalchemy.sql.expression import func
from sqlalchemy import or_

just_one = Blueprint('random_word', __name__, )


@just_one.route('/justone', methods=['GET', 'POST'])
def get_word_from_db():
    # Set dictionary to hold difficulty selection. A future idea: change to a class Difficulty.
    difficulties = [{'Kids': ''}, {'Adults': ''}, {'Extreme': ''}]

    if request.method == 'POST':
        # Get the difficulty from radio button selector
        selected_difficulty = request.form.get('difficulty_radio')

        # If value was not None, the user has clicked "Next" and thus want to continue with this difficulty.
        if selected_difficulty:
            session['difficulty'] = selected_difficulty

        # If the user wanted to change the difficulty of the previous word, let's update the SQL row.
        if 'too_difficult' in request.form.keys():
            prev_values = request.form['too_difficult'].split('.')

            # Double check that the list contains only two values (e.g. 'kids' and 9872)
            if len(prev_values) == 2:

                # Unpack the list
                prev_too_diff_for, prev_id = prev_values

                # Parse the input
                if prev_too_diff_for == 'Kids':
                    new_diff = 1
                elif prev_too_diff_for == 'Adults':
                    new_diff = 2
                else:
                    new_diff = None

                # Update the row
                if new_diff:
                    db.session.query(Word).filter_by(word_id=prev_id).update({'difficulty': new_diff})
                    db.session.commit()
                    print(f'Row id #{prev_id} updated with a new difficulty as {new_diff}')

    # Set default difficulty if there is no cookie yet
    selected_difficulty = session.get('difficulty') or 'Adults'

    # Iterate through all difficulties. The selected will have value 'checked', others ''.
    difficulties, difficulty_number = update_difficulty(difficulties, selected_difficulty)

    if difficulty_number is not None:
        # Get a Just One compatible word from the corpus
        query_result = Word.query.filter(Word.difficulty <= difficulty_number) \
            .filter(or_(Word.is_subs, Word.is_name)) \
            .order_by(func.random()) \
            .limit(1).first()
        query_result, query_index = query_result.word, query_result.word_id
    else:
        query_result = 'Forbidden FORM POST. Does not match to the keys in dictionary. Stop touching my cookies!'

    return render_template("justone.html", difficulties=difficulties, query_result=query_result,
                           query_index=query_index)
