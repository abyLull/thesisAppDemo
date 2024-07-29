import os

default_app_config = 'myapp.apps.MyAppConfig'

if os.environ.get('RUN_MAIN'):
    from . import custom_filters