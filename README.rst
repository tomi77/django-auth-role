================
django-auth-role
================

.. image:: https://codeclimate.com/github/tomi77/django-auth-role/badges/gpa.svg
   :target: https://codeclimate.com/github/tomi77/django-auth-role
   :alt: Code Climate
.. image:: https://travis-ci.org/tomi77/django-auth-role.svg?branch=master
   :target: https://travis-ci.org/tomi77/django-auth-role
.. image:: https://coveralls.io/repos/github/tomi77/django-auth-role/badge.svg?branch=master
   :target: https://coveralls.io/github/tomi77/django-auth-role?branch=master

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
       def fetch_role_permissions(self, user_obj):
           return Permission.objects.filter(group__roles__myusers__user=user_obj)

And add it to `AUTHENTICATION_BACKENDS`.

.. sourcecode:: python

   AUTHENTICATION_BACKENDS = (
       'app.MyBackend',
   )
