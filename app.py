from flask import Flask, render_template
from databases.shared import db

from config import Config
from views.raidersofthenorthsea import raidersofthenorthsea
from views.just_one import just_one

# Set up the Flask App
app = Flask(__name__)

# Configs and blueprints
app.config.from_object(Config)
app.register_blueprint(raidersofthenorthsea)
app.register_blueprint(just_one)

# Instantiate the Sqlite DB connector
db.init_app(app)

@app.route("/")
def portal():
    links = [('raiders', 'Raiders of the North Sea'),
             ('randomword', 'Random Word')]
    return render_template("portal.html", links=links)


if __name__ == '__main__':
    app.run(debug=True)
