"""Configuration file for the package."""
import os
import time

from setuptools import find_packages, setup
from setuptools_scm.version import guess_next_version


def read(file_name):
    """Read in the supplied file name from the root directory.

    Args:
        file_name (str): the name of the file

    Returns: the content of the file
    """
    this_dir = os.path.dirname(__file__)
    file_path = os.path.join(this_dir, file_name)
    with open(file_path) as f:
        return f.read()


def version_scheme(version):
    """Version scheme hack for setuptools_scm.

    Appears to be necessary to due to the bug documented here: https://github.com/pypa/setuptools_scm/issues/342

    If that issue is resolved, this method can be removed.
    """
    if version.exact:
        return version.format_with("{tag}")
    else:
        _super_value = version.format_next_version(guess_next_version)
        now = int(time.time())
        return _super_value + str(now)


def local_version(version):
    """Local version scheme hack for setuptools_scm.

    Appears to be necessary to due to the bug documented here: https://github.com/pypa/setuptools_scm/issues/342

    If that issue is resolved, this method can be removed.
    """
    return ""


setup(
    name="atcf-data-parser",
    description="Parse a-deck data posted online by the Automated Tropical Cyclone Forecasting System",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="your name",
    author_email="your@email.com",
    url="http://www.github.com/palewire/atcf-data-parser",
    project_urls={
        "Maintainer": "https://github.com/palewire/",
        "Source": "https://github.com/palewire/atcf-data-parser",
        "Tracker": "https://github.com/palewire/atcf-data-parser/issues",
    },
    packages=find_packages(),
    setup_requires=["setuptools_scm"],
    use_scm_version={"version_scheme": version_scheme, "local_scheme": local_version},
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=[
        "pandas",
        "numpy",
        "rich",
        "click",
        "requests",
        "retry",
    ],
    entry_points={
        "console_scripts": [
            "atcf-data-parser=atcf_data_parser.cli:cli",
        ],
    },
)
