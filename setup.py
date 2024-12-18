# coding: utf-8

import os
from setuptools import setup, find_packages

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

setup(
        name='django-pygments',
        version='0.8',
        description='Django app that provides a template tag and 2 filters for \
                doing syntax highlighting with Pygments',
        long_description=readme,
        long_description_content_type="text/markdown",
        author='Ștefan Talpalaru',
        author_email='stefantalpalaru@yahoo.com',
        url='http://github.com/stefantalpalaru/django-pygments',
        packages=find_packages(),
        include_package_data=True,
        install_requires=['pygments'],
        classifiers=[
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 3',
            'Framework :: Django',
            ],
        )
