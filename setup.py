from setuptools import setup, find_packages

import mezzanine_tools

setup(
    name='mezzanine_tools',
    version=mezzanine_tools.__version_str__,
    packages=find_packages(exclude=('sandbox',)),
    url='',
    license='BSD',
    author='Jakub Skaryd',
    author_email='skaryd@gmail.com',
    description='Mezzanine powertools'
)
