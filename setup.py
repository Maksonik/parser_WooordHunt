from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="wooordhunt_parser",
    version="0.3.0",
    author="<athour name>",
    author_email="<author email>",
    description="This Python library allows you to fetch detailed descriptions of words from www.wooordhunt.ru.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
)