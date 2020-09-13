import os


def generate_db_uri(db_folder, db_filename):
    # Get this file's location
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_full_path = os.path.join(basedir, db_folder, db_filename)
    return 'sqlite:///' + db_full_path


class Config(object):
    # Generate absolute path to /home/user/db_folder/corpus.db
    SQLALCHEMY_DATABASE_URI = generate_db_uri(db_folder='databases', db_filename='corpus.db')

    # Disable Flask-SQLAlchemy's event system. It consumer resources for no benefit.
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Remember to set this in systemd file when running tabletop.wtf in public internet.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'only_in_local_dev_secret'
