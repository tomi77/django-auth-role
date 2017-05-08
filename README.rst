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

Add ``authrole`` to `INSTALLED_APPS` (``django.contrib.auth`` and ``django.contrib.contenttypes`` are also required) and ``AuthRoleBackend`` to `AUTHENTICATION_BACKENDS`.

.. sourcecode:: python

   INSTALLED_APPS = [
       ...
       'django.contrib.contenttypes',
       'django.contrib.auth',
       'authrole',
   ]

   AUTHENTICATION_BACKENDS = (
       'authrole.auth.backends.AuthRoleBackend',
   )

Extend ``auth.User``.

.. sourcecode:: python

   from authrole.mixins import RoleMixin
   from django.db import models

   class MyUser(RoleMixin, models.Model):
       user = models.OneToOneField('auth.User', related_name='user')

or create new auth user model:

.. sourcecode:: python

   from authrole.mixins import RoleMixin
   from django.contrib.auth.models import AbstractUser
   from django.db import models

   class MyUser(RoleMixin, AbstractUser):
       pass

In this case remember to set ``AUTH_USER_MODEL`` to Your model.

Create tables.

.. sourcecode:: sh

   ./manage.py migrate
