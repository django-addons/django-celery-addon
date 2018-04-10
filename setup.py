# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


# from https://gist.github.com/techtonik/4066623
def get_version(relpath):
    """Read version info from a file without importing it"""
    from os.path import dirname, join

    if '__file__' not in globals():
        # Allow to use function interactively
        root = '.'
    else:
        root = dirname(__file__)

    # The code below reads text file with unknown encoding in
    # in Python2/3 compatible way. Reading this text file
    # without specifying encoding will fail in Python 3 on some
    # systems (see http://goo.gl/5XmOH). Specifying encoding as
    # open() parameter is incompatible with Python 2

    # cp437 is the encoding without missing points, safe against:
    #   UnicodeDecodeError: 'charmap' codec can't decode byte...

    for line in open(join(root, relpath), 'rb'):
        line = line.decode('cp437')
        if '__version__' in line:
            if '"' in line:
                # __version__ = "0.9"
                return line.split('"')[1]
            elif "'" in line:
                return line.split("'")[1]


setup(
    name="django-celery-addon",
    version=get_version('django_celery_addon/__init__.py'),
    description='An opinionated Celery setup bundled as an Django Addon..',
    author='Divio AG',
    author_email='info@divio.ch',
    url='https://github.com/django-addons/django-celery-addon',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=(
        'django-addons>=2',
        'celery==4.1.0',
        'django-celery-beat',
        'django-celery-results',
    ),
    entry_points='''
        [console_scripts]
        django-celery-addon=django_celery_addon.cli:main
    ''',
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django :: 2.0',
    ],
)
