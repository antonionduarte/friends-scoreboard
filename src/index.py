from flask import (
    Blueprint, url_for, redirect,
    g
)

# What needs to happen: 
# - You can only see the Scoreboard page if you're logged in
# - Form to introduce new entry into the Scoreboard (only if logged in as well)

blueprint = Blueprint('index', __name__, url_prefix=('/'))

@blueprint.route('')
def index():
    if g.user == None:
        return redirect(url_for('auth.login'))
    else:
        return redirect(url_for('score.scoreboard'))

