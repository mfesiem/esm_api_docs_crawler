#! /usr/bin/env python3

from setuptools import setup
import pathlib


# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='esm_api_docs_crawler',
    description="Crawl the ESM API docs and extract all resources. ",
    url='https://github.com/mfesiem/esm_api_docs_crawler',
    maintainer='tristanlatr',
    version='1.1',
    packages=['esm_api_docs_crawler',],
    install_requires=[
          'scrapy', 'scrapy-crawl-once', 
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    license='The MIT License',
    long_description=README,
    long_description_content_type="text/markdown"
)