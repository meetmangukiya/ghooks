from setuptools import find_packages, setup

with open("README.rst") as f:
    long_description = f.read()

setup(name = 'ghooks',
    version = '0.1',
    description = "GitHub hooks made simpler to handle!",
    long_description = long_description,
    author="Meet Mangukiya",
    author_email="meetmangukiya98@gmail.com",
    url="https://github.com/meetmangukiya/ghooks",
    license = "MIT",
    packages=find_packages(),
    entry_points={}
    )
