from setuptools import setup

setup(
    name='netwey-cli',
    version='0.1.0',
    py_modules=['netwey'],
    install_requires=[
        'Click',
        'bs4',
        'requests',
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'netwey-cli = netwey:cli',
        ],
    },
)
