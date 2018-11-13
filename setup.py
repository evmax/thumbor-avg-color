# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='thumbor-avg-color',
    version='0.0.1',
    url='http://github.com/evmax/thumbor-avg-color',
    license='MIT',
    author='Max Elakhov',
    description='Thumbor average color detector',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'thumbor',
    ],
    extras_require={},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
