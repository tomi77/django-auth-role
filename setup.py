from codecs import open

from setuptools import setup, find_packages

setup(
    name='django-auth-role',
    version='0.3.0',
    author='Tomasz Jakub Rup',
    author_email='tomasz.rup@gmail.com',
    url='https://github.com/tomi77/django-auth-role',
    description='Add roles to django-auth',
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Framework :: Django :: 1.4',
        'Framework :: Django :: 1.5',
        'Framework :: Django :: 1.6',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    license='MIT',
    packages=find_packages(exclude=['tests.*', 'tests']),
    package_data={
        'authrole': [
            'locale/pl/LC_MESSAGES/*',
        ]
    },
    install_requires=[
        'django>=1.4',
    ]
)
