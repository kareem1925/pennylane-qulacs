import re

from setuptools import setup
import os

with open('./pennylane_qulacs/__init__.py') as f:
    version, = re.findall('__version__ = \'(.*)\'', f.read())

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='pennylane_qulacs',
    description='PennyLane plugin for Qulacs',
    version=version,
    long_description=long_description,
    install_requires=[
        'pennylane>=0.5.0',
        'numpy',
        'scipy',
        ('qulacs-gpu' if os.path.exists('/proc/driver/nvidia/version') else 'qulacs')
    ],
    packages=['pennylane_qulacs'],
    entry_points={
        'pennylane.plugins': [
            'qulacs.simulator = pennylane_qulacs.qulacs_device:QulacsDevice'
        ]
    }
)
