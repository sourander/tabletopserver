from flask import Flask, render_template

from config import Config
from views.raidersofthenorthsea import raidersofthenorthsea

app = Flask(__name__)

app.config.from_object(Config)
app.register_blueprint(raidersofthenorthsea)


@app.route("/")
def portal():
    links = [('raiders', 'Raiders of the North Sea')]

    return render_template("portal.html", links=links)


if __name__ == '__main__':
    app.run()
