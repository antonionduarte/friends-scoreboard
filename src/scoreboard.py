from flask import (
    Blueprint, render_template, session, request,
)

# What needs to happen: 
# - You can only see the Scoreboard page if you're logged in
# - Form to introduce new entry into the Scoreboard (only if logged in as well)

blueprint = Blueprint('score', __name__, url_prefix=('/score'))

@blueprint.route('')
def scoreboard():
    return 'Scoreboard'
