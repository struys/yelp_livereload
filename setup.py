# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup


setup(
    name='yelp_livereload',
    description=(
        'livereload utils used at Yelp'
    ),
    version='0.1.0',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],

    packages=find_packages('.', exclude=('tests*',)),
    install_requires=[
        'webob',
        'argparse',
        'livereload',
    ],
    package_data={
        'yelp_livereload': [
            'assets/livereload-scss.js',
        ],
    },
    entry_points={
        'console_scripts': [
            'yelp-livereload = yelp_livereload.cli:main',
        ],
    },
)
