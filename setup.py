from setuptools import setup

setup(
    name='netwey-cli',
    version='0.1.1',
    py_modules=['netwey'],
    python_requires='>=3',
    author="Andres Vargas - zodman",
    author_email="zodman@gmail.com",
    url="https://github.com/zodman/netwey-cli",
    long_description=("netwey-cli it fetch the information for your"
                      "netwey.com.mx account"),
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
