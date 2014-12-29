import os, sys
from setuptools import setup

setup(
    name='reddit_comment_scraper',
    version='1.2',
    author='Jesse Farmer',
    author_email='jesse@20bits.com',
    license='MIT License',
    py_modules=['scrape_comments'],
    install_requires=[
        'unicodecsv==0.9.4',
        'praw==2.1.19'
    ]
)
