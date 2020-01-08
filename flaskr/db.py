import sqlite3
import click

# g is used to store data that might be accessed by multiple functions during the request
# current_app points to the Flask application handling the request

from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        # establishes a connection to the file pointed at by the database configuration key
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # tell the connection to return rows that behave like dicts
        # allows accessing the columns by name
        g.db.row_factory = sqlite3.Row
    return g.db

# checks to see if a connection was created
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()
    # opens file relative to the flaskr package
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
# defines a command line command called init-db which calls init_db function
@click.command('init-db')
@with_appcontext
def init_db_command():
    """ Clear the existing data and create new tables """
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    # tells Flask to call that function when cleaning up after returning a response
    app.teardown_appcontext(close_db)
    # adds a new command that can be called with Flask
    app.cli.add_command(init_db_command)