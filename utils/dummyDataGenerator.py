from mixer.backend.flask import mixer
from utils.initDB import *

mixer.init_app(app)


def run_generator():
    for i in range(50000):
        if i % 1000 == 0:
            print('Generated: {} items for "parsing"'.format(i))
        mixer.blend(Record, event_name="parsing")
    for i in range(33333):
        if i % 1000 == 0:
            print('Generated: {} items for "uploading"'.format(i))
        mixer.blend(Record, event_name="uploading")
