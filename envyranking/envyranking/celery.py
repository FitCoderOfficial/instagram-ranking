from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
from celery.schedules import crontab 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'envyranking.settings')
  
app = Celery('envyranking')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
        'add-every-30-minutes-contrab': {
            'task': 'check_new_update_ted',
            'schedule': crontab(minute='*/30'),
            },
            }

def debug_task(self):
    print('Request: {0!r}'.format(self.request))
