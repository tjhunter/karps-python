from setuptools import setup, find_packages

setup(
    name='karps',
    version='0.2.0',
    packages=['karps', 'karps.functions_std', 'karps.proto'],
    install_requires=['grpcio', 'pandas', 'six', 'future'],
    author="Timothy Hunter",
    author_email="me@example.com",
    license='Apache 2.0',
    long_description=open('README.md').read(),
)