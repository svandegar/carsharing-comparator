from setuptools import setup

setup(
    name='Car-sharing compare',
    packages=['backend'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)