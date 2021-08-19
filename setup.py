from setuptools import setup

setup(
    name='netwey-cli',
    version='0.1.0',
    py_modules=['netwey'],
    author="Andres Vargas - zodman",
    author_email="zodman@gmail.com",
    long_description=("netwey-cli it fetch the information for your netwey.com.mx"
                     " account"),
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
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
