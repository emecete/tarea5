
from setuptools import setup, find_packages

setup(
    name='tarea5',
    version='1.0.0',
    description='Factorial and Mocking',
    url='https://github.com/emecete/tarea5',
    author='María del Rocío Cabello Toscano',
    author_email='mcttuf0@uma.es',
    license='MIT',
    python_requires='>=3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Programming Language :: Python :: 3.6'
    ],
    packages=find_packages(exclude=["test.*", "tests"]),
)
