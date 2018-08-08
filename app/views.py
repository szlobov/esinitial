from flask import render_template

from app import app
import requests
from config import ES_HOST


@app.route('/')
def index_page():
    return render_template('indexpage.html')


@app.route('/es-data/<idx_name>', methods=['GET'])
def es_indexes(idx_name=None):
    res = requests.get('{}/{}'.format(ES_HOST, idx_name))
    data = res.json()
    return render_template('esindex.html', idx_data=data)
