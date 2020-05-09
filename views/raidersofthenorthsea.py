from flask import Blueprint, render_template, request

raidersofthenorthsea = Blueprint('raiders_of_the_north_sea', __name__,)

@raidersofthenorthsea.route('/raiders', methods=['GET', 'POST'])
def raiders():

    extensions = [('hall_of_heroes', 'Hall of Heroes'),
                  ('field_of_fame', 'Fields of Fame')]
    tokens = []
    if request.method == 'POST':
        addons = request.form.getlist('my_checkbox')
        print(addons)
        tokens = ['gold', 'stone']


    return render_template("raiders.html", extensions=extensions, tokens=tokens)