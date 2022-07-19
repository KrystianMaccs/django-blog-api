import os

from django.conf import settings

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog_api.settings")

app = Celery("blog_api", broker=settings.BROKER_URL)

# Using a string here means the worker will not have to 
# pickle the object when iusing windows

app.config_from_object("django.conf:settings")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))