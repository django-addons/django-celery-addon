# -*- coding: utf-8 -*-
from __future__ import absolute_import

__version__ = '3.1.25.5'

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app  # noqa
