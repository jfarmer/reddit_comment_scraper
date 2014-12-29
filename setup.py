import os, sys
from setuptools import setup

setup(
    name='reddit_comment_scraper',
    version='2.0.5',
    description='A simple Reddit-scraping script',
    url='https://github.com/jfarmer/reddit_comment_scraper',
    author='Jesse Farmer',
    author_email='jesse@20bits.com',
    license='MIT',

    packages=['reddit_comment_scraper'],

    install_requires=[
        'unicodecsv==0.9.4',
        'praw==2.1.19'
    ],

    entry_points={
        'console_scripts': [
            'scrape_comments=reddit_comment_scraper:main'
        ]
    },

    classifiers=[
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Environment :: Console',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows :: Windows 7',
        'Operating System :: Microsoft :: Windows :: Windows Vista',
    ],
)
