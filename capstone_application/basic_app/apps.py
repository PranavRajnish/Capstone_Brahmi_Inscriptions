from django.apps import AppConfig
from .pipeline import load_model_60
import os
from django.conf import settings

class BasicAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'basic_app'

    def ready(self) -> None:
        if os.environ.get('RUN_MAIN'):
            print("STARTUP AND EXECUTE HERE ONCE.")
            model_60 = load_model_60()
            settings.MODEL_60 = model_60


