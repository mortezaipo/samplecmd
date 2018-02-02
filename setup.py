"""Package setup."""
from setuptools import setup, find_packages

setup(
    name="samplecmd",
    version="1.0.0",
    description="SampleCMD is a CLI application which prepares sample "
                "commands for users based on search words.",
    author="Morteza Nourelahi Alamdari <me@mortezana.com>",
    keywords="samplecmd cmd cli search",
    license="GPLv3.0",
    url="https://github.com/mortezaipo/samplecmd/",
    packages=find_packages(),
    install_requires=['colorclass', 'lxml', 'requests'],
    data_files=[("sites", ["sites/bashoneliner.ini",
                           "sites/commandlinefu.ini"])],
    python_requires='>=3',
    entry_points={
        "console_scripts": [
            "samplecmd=samplecmd.samplecmd:main",
        ],
    })