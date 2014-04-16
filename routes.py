import os
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/dailyRamblingWords')
def words():
    import dailyRamblingWords as drw

    return jsonify(drw.get_week_words())
