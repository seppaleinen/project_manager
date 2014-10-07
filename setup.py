from setuptools import setup, find_packages
    
setup(
    name='pythontest',
    version='0.0.1',
    author='David Eriksson',
    author_email='david.eriksson@swedenmail.com',
    packages=find_packages(),
    scripts=[ 'bin/binfile' ],
    url='www.google.se',
    zip_safe=False,
    license='GPLv3',
    description='Python test.',
    install_requires=[],
    tests_require=[],
    #install_requires=[
    #    "args>=0.1.0",
    #    "clint>=0.3.3",
    #    "requests>=2.2.0",
    #    "wsgiref>=0.1.2",
    #    "xerox"
    #],
    test_suite="tests",
)
