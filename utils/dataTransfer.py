from elasticsearch.helpers import bulk

from app import app
from flask_sqlalchemy import SQLAlchemy

from config import ES_HOST
from utils.initDB import Record
from elasticsearch import Elasticsearch

db = SQLAlchemy(app)
es = Elasticsearch([ES_HOST])

# Generator for DB. Yields by 10k chunks from db.
records = db.session.query(Record).yield_per(10000)

actions = [
    {
        "_index": "parquet_data",
        "_type": "record",
        "_source": {
            "event_name": r.event_name,
            "min_result": r.min_result,
            "max_result": r.max_result,
            "date": r.date
        }
    }
    for r in records
]


def process_records():
    bulk(es, actions=actions)
