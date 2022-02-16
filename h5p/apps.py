from pathlib import Path
from django.apps import AppConfig
from django.conf import settings
import os

class H5PConfig(AppConfig):
    name = 'h5p'


    #def ready(self):
       # CONTENT_DIR =  os.path.join(settings.MEDIA_ROOT, 'xapi')
       # print(CONTENT_DIR)
       # if not CONTENT_DIR.exists():
       #     CONTENT_DIR.mkdir(parents=True, exist_ok=True)
