from __future__ import absolute_import

import os

from blog_api.settings import base

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog_api.settings.development")

app = Celery("blog_api")

# Using a string here means the worker will not have to 
# pickle the object when using windows

app.config_from_object("blog_api.settings.development", namespace="CELERY"),
app.autodiscover_tasks(lambda: base.INSTALLED_APPS)

"""@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))"""