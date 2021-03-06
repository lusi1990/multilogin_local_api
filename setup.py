# coding: utf-8

"""
    Multilogin Local REST API

    Multilogin Local REST API can be used in order to start, stop, share, clone browser profile/-s. You can also check if the profile is already running on your machine by using checkProfileRunning endpoint and import cookies by using cookieImportJSON/cookieImportNetscape endpoint.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "multilogin_local_api"
VERSION = "1.0.4"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]

setup(
    name=NAME,
    version=VERSION,
    description="Multilogin Local REST API",
    author_email="lusi2114@gmail.com",
    author="Master Lu",
    url="https://github.com/lusi1990/multilogin_local_api",
    keywords=["Swagger", "Multilogin Local REST API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Multilogin Local REST API can be used in order to start, stop, share, clone browser profile/-s. You can also check if the profile is already running on your machine by using checkProfileRunning endpoint and import cookies by using cookieImportJSON/cookieImportNetscape endpoint.  # noqa: E501
    """
)
