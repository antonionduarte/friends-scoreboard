from flask import (
    Blueprint, render_template, session, request,
)

# What needs to happen: 
# - You can only see the Scoreboard page if you're logged in
# - Form to introduce new entry into the Scoreboard (only if logged in as well)

blueprint = Blueprint('score', __name__, url_prefix=('/score'))

data = {'data' : [
    {
        'label': 'Francisco',
        'data': [0, 10, 5, 2, 20, 33],
        'id': 0

    },
    {
        'label': 'Manuel',
        'data': [4, 16, 2, 2, 0, 4],
        'id': 1
    },
    {
        'label': 'António',
        'data': [3, 12, 1, 3, 26, 20],
        'id': 2
    },
]}

@blueprint.route('')
def scoreboard():
    return render_template('scoreboard.html')

@blueprint.route('/current-score', methods=('GET', 'POST'))
def current_score():
    # TODO: Very strongly requires authentication
    return data

def calculate_score():
    return None
