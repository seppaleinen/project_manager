from setuptools import setup
    
setup(
    name='pyth',
    version='0.0.14',
    author='David Eriksson',
    author_email='david.eriksson@swedenmail.com',
    packages=[ 'package' ],
    scripts=[ 'bin/binfile' ],
    url='www.google.se',
    license='LICENSE.txt',
    description='Save your code snippets in the cloud.',
    #install_requires=[
    #    "args>=0.1.0",
    #    "clint>=0.3.3",
    #    "requests>=2.2.0",
    #    "wsgiref>=0.1.2",
    #    "xerox"
    #],
    test_suite="tests",
)
