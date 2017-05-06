================
django-auth-role
================

Add roles to django-auth

Installation
============

.. sourcecode:: sh

   pip install django-auth-role

Quick start
===========

Add ``authrole`` to `INSTALLED_APPS`. ``django.contrib.auth`` and ``django.contrib.contenttypes`` are also required.

.. sourcecode:: python

   INSTALLED_APPS = [
       ...
       'django.contrib.contenttypes',
       'django.contrib.auth',
       'authrole',
   ]

Extend ``auth.User``.

.. sourcecode:: python

   from django.db import models

   class MyUser(models.Model):
       role = models.ForeignKey('authrole.Role', related_name='myusers')
       user = models.OneToOneField('auth.User', related_name='user')

Create tables.

.. sourcecode:: sh

   ./manage.py migrate

Extend Your own authentication backend.

.. sourcecode:: python

   from authrole.auth.backends import BaseAuthRoleBackend

   class MyBackend(BaseAuthRoleBackend):
       def fetch_permission(self, user_obj):
           return Permission.objects.filter(group__roles__myusers__user=user_obj)

And add it to `AUTHENTICATION_BACKENDS`.

.. sourcecode:: python

   AUTHENTICATION_BACKENDS = (
       'app.MyBackend',
   )
