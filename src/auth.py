import functools 
import click 

from flask import (
        Blueprint, flash, g, redirect, render_template, 
        request, session, url_for 
)
from werkzeug.security import check_password_hash, generate_password_hash 
from src.database import get_db
from flask.cli import with_appcontext

SELECT_USER_USERNAME = 'SELECT * FROM user WHERE username = ?'
SELECT_USER_ID = 'SELECT * FROM user WHERE id = ?'
INSERT_USER = 'INSERT INTO user (username, password, admin) VALUES (?, ?, ?)'

blueprint = Blueprint('auth', __name__, url_prefix='/auth')


# Routes:


@blueprint.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        admin = request.form['admin']
        database = get_db()
        error = None

        if not g.user['admin']:
            error = 'Only administrators can create new accounts'
        if not username: 
            error = 'Username is required.'
        elif not password: 
            error = 'Password is required'

        if error is None:
            try: 
                database.execute(INSERT_USER, (username, generate_password_hash(password), eval(admin)),)
                database.commit()
            except database.IntegrityError:
                error = f"User {username} is already registered."
            else: 
                return redirect(url_for("auth.login"))

        flash(error)
    return render_template('auth/register.html')


@blueprint.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        database = get_db()
        error = None
        user = database.execute(SELECT_USER_USERNAME, (username,)).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None: 
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)
    return render_template('auth/login.html')


@blueprint.before_app_request 
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(SELECT_USER_ID, str(user_id)).fetchone()


@blueprint.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view


# CLI Commands:


@click.command('add-admin')
@click.argument('username')
@click.argument('password')
@with_appcontext
def add_admin_command(username, password):
    database = get_db()
    error = None

    if not username: 
        error = 'Username is required.'
    elif not password: 
        error = 'Password is required'

    if error is None:
        try: 
            database.execute(INSERT_USER, (username, generate_password_hash(password), True),)
            database.commit()
        except database.IntegrityError:
            error = f"User {username} is already registered."

    if error is None: 
        click.echo('Successfully registered Admin account')
    else:
        click.echo(error)


@click.command('add-user')
@click.argument('username')
@click.argument('password')
@with_appcontext
def add_user_command(username, password):
    database = get_db()
    error = None

    if not username: 
        error = 'Username is required.'
    elif not password: 
        error = 'Password is required'

    if error is None:
        try: 
            database.execute(INSERT_USER, (username, generate_password_hash(password), False),)
            database.commit()
        except database.IntegrityError:
            error = f"User {username} is already registered."

    if error is None: 
        click.echo('Successfully registered User account')
    else:
        click.echo(error)


def init_auth(app):
    app.cli.add_command(add_admin_command)
    app.cli.add_command(add_user_command)
