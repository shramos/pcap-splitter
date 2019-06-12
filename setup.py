# File from pcap-splitter project
# Copyright (C) 2019 Santiago Hernandez Ramos <shramos@protonmail.com>
# For more information about the project: https://github.com/shramos/pcap-splitt

from setuptools import setup
import setuptools

setup(
    name="pcap_splitter",
    version="1.0.0",
    license="GNU",
    description="Pcap-splitter allows you to split a _.pcap_ file into subsets of _.pcap_ files based on sessions, flows, ip addresses, number of bytes, number of network packets...",
    platforms=["Linux", "Windows", "MacOS"],
    url="https://github.com/shramos/pcap-splitter",
    author="Santiago Hernandez Ramos",
    author_email="shramos@protonmail.com",
    packages=setuptools.find_packages(),
    keywords=[
        'pcap',
        'split',
        'network',
        'packet',
        'modification',
        'manipulation',
        'modify',
        'flows',
        'sessions',
        'ip',
        'divide',
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
