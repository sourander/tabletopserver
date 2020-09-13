from flask import Blueprint, render_template, request
from games.raiders.raiders import raiders_config_menu
from games.raiders.modules.board import Board
from games.raiders.modules.bag import Bag

raidersofthenorthsea = Blueprint('raiders_of_the_north_sea', __name__,)

@raidersofthenorthsea.route('/raiders', methods=['GET', 'POST'])
def raiders():

    extensions = [('hall_of_heroes', 'Hall of Heroes'),
                  ('field_of_fame', 'Fields of Fame')]
    locations = []

    if request.method == 'POST':
        # Get checkbox statuses
        selected_addons = request.form.getlist('my_checkbox')

        # Generate pool of tokens and pool of locations in Raiders of the North
        pool, location_pool = raiders_config_menu(selected_addons)

        # Instantiate
        bag = Bag(pool)
        board = Board(location_pool, bag)

        # Get locations as a list of dictionary
        board_split = [6,6,5,3,3]
        locations = board.get_locations(board_split)

    return render_template("raiders.html", extensions=extensions, locations=locations)