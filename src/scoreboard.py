from flask import (
    Blueprint, render_template,
)

import datetime

from src.database import get_db 

# What needs to happen: 
# - You can only see the Scoreboard page if you're logged in
# - Form to introduce new entry into the Scoreboard (only if logged in as well)

SELECT_USERS = 'SELECT * FROM user'

blueprint = Blueprint('score', __name__, url_prefix=('/score'))

@blueprint.route('')
def scoreboard():
    # TODO: Very strongly required authentication
    return render_template('scoreboard.html')


@blueprint.route('/current-score', methods=('GET', 'POST'))
def current_score():
    # TODO: Very strongly requires authentication
    database = get_db()
    now = datetime.datetime.now()
    users = database.execute(SELECT_USERS).fetchall()
    data = { 'data' : [] }
    for user in users: 
        score = calculate_score(now.month, now.year, user[0])
        data['data'].append({
            'label': user[4],
            'data': score,
            'id': user[0]
        })
    return data 


# Calculates a user's score for a specific month
# TODO: Maybe try to make it so the month in an entry can be in 0X or X format in case 
#       it's a single digit month.
def calculate_score(month, year, user_id):
    database = get_db()
    with open('./src/sql/query_month.sql') as query: 
        query_str = query.read()
        init_date = '{}-{}-1'.format(year, month)
        final_date = '{}-{}-31'.format(year, month)
        entries = database.execute(query_str, (init_date, final_date, user_id)).fetchall()
        scores = [0] * 31 
        curr_score = 0
        for entry in entries: 
            day = int(entry[2].split('-')[2])
            scores[day - 1] += entry[0]
        final_scores = [0] * 31
        for i in range(0, 31): 
            curr_score += scores[i]
            final_scores[i] = curr_score
        return final_scores
