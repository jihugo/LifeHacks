"""Setup file for mytools packages"""
from setuptools import setup


def parse_requirements(filename):
    """load requirements from a pip requirements file"""
    lineiter = (line.strip() for line in open(filename, encoding="UTF8"))
    return [line for line in lineiter if line and not line.startswith("#")]


setup(name="mytools", version="1.0", packages=parse_requirements("requirements.txt"))
