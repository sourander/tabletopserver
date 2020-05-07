from flask import Blueprint, render_template, abort

raidersofthenorthsea = Blueprint('raiders_of_the_north_sea', __name__,)

@raidersofthenorthsea.route('/raiders')
def raiders():
    return render_template("raiders.html")