from setuptools import setup, find_packages

setup(
    name='tommieaudioslicer',
    version='1.0.0',
    description='SimpleSlicer',
    author='Tommie Introna',
    author_email='tommie@blackshuck.co',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'soundfile',
    ],
)