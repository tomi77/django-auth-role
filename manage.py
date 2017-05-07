#!/usr/bin/env python
import os

if os.environ.get('DJANGO_SETTINGS_MODULE') is None:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.extend.settings'
from django.core import management

if __name__ == "__main__":
    management.execute_from_command_line()
