from setuptools import setup
    
setup(
    name='python',
    version='1.0-SNAPSHOT',
    author='David Eriksson',
    author_email='david.eriksson@swedenmail.com',
    packages=[ 'python_dir' ],
    scripts=[ 'scripts/binfile' ],
    url='www.google.se',
    zip_safe=False,
    license='GPLv3',
    description='Python test.',
    install_requires=[
        "gitPython==1.0.1"
    ],
    tests_require=[
        "gitPython==1.0.1"
    ],
    #install_requires=[
    #    "args>=0.1.0",
    #    "clint>=0.3.3",
    #    "requests>=2.2.0",
    #    "wsgiref>=0.1.2",
    #    "xerox"
    #],
    test_suite='tests',
)