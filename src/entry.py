from flask import (
    Blueprint, render_template, session, request,
)
from flask.cli import with_appcontext

import click
import sqlite3
import datetime

from src.database import get_db 

INSERT_ENTRY = 'INSERT INTO entry (score, user_id, entry_date) VALUES (?, ?, ?)'

blueprint = Blueprint('entry', __name__, url_prefix=('/entry'))

# add entry with PUT and get entry JSON with GET for no reason whatsoever
@blueprint.route('')
def scoreboard():
    return render_template('scoreboard.html')


@click.command('add-entry')
@click.argument('timestamp')
@click.argument('user_id')
@click.argument('score')
@with_appcontext
def add_entry_command(timestamp, user_id, score):
    database = get_db()
    error = None
    if not user_id: 
        error = "User ID is required."
    if not timestamp: 
        error = "Timestamp is required"
    if not score: 
        error = "Score is required"
    if error is None: 
        try: 
            database.execute(INSERT_ENTRY, (score, user_id, timestamp))
            database.commit()
        except: 
            click.echo('Unexpected error occurred')
        return None
    else:
        click.echo(error)


def init_entries(app):
    app.cli.add_command(add_entry_command)
