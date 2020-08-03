from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'envyranking.settings')
  
app = Celery('envyranking')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


def debug_task(self):
    print('Request: {0!r}'.format(self.request))
