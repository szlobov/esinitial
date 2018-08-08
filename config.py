import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
ADMINS = ['list of error emails']

SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost:3306/esdb"

ES_HOST = "http://127.0.0.1:9200"
KIBANA_HOST = "http://127.0.0.1:5601"

KIBANA_BIN_DIR="/opt/kibana/bin/"
ELASTIC_BIN_DIR="/opt/elastic/bin/"

PARQUET_FILEDIR = ""
