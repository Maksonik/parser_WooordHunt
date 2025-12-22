from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="wooordhunt_parser",
    version="0.4.0",
    author="<author name>",
    author_email="<author email>",
    description="This Python library allows you to fetch detailed descriptions of words from www.wooordhunt.ru.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4>=4.12.3,<5.0.0",
        "lxml>=5.3.0,<6.0.0",
        "httpx>=0.28.1,<0.29.0",
    ],
    extras_require={
        "dev": [
            "ruff>=0.8.6,<1.0.0",
            "pytest-asyncio>=0.25.2,<0.26.0",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)