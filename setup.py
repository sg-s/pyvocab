"""setup file"""

from setuptools import find_packages, setup

setup(
    name="pyvocab",
    version="22.7.20",
    packages=find_packages(exclude=("tests", "docs")),
    description="simple vocabulary builder in python",
    url="https://github.com/sg-s/pyvocab",
    author="Srinivas Gorur-Shandilya",
    author_email="code@srinivas.gs",
    install_requires=[
        "pandas>=1.3.2",
        "watchdog",
        "streamlit>=1.11.0",
        "interrogate>=1.0",
        "python-Levenshtein",
        "pycore @ git+https://github.com/sg-s/pycore.git",
    ],
    extras_require={
        "dev": [
            "pytest",
        ]
    },
)
