import os.path

try:
    import setuptools
    from setuptools import setup
except ImportError:
    setuptools = None
    from distutils.core import setup

from supportbot import __version__


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))


kwargs = {}

if setuptools is not None:
    python_requires = ">=3.6"
    kwargs["python_requires"] = python_requires

with open_file("README.md") as f:
    kwargs["long_description"] = f.read()
    kwargs["long_description_content_type"] = "text/markdown"

setup(
    name="supportbot",
    version=__version__,
    description="Supportbot to support questions and their answers",
    author="Kaizhao Zhang",
    author_email="zhangkaizhao@gmail.com",
    url="https://github.com/zhangkaizhao/supportbot",
    license="MIT",
    packages=[
        "supportbot",
        "supportbot.full_text_search",
        "supportbot.fuzzy_matching",
    ],
    install_requires=[
        "fuzzywuzzy[speedup]>=0.17.0",
        "jieba>=0.39",
        "Whoosh>=2.7.4",
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    **kwargs
)
