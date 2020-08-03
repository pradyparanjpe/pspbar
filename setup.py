#!/usr/bin/env python3
# -*- coding:utf-8; mode:python -*-
#
# Copyright 2020 Pradyumna Paranjape
# This file is part of pspbar.
#
# pspbar is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pspbar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pspbar.  If not, see <https://www.gnu.org/licenses/>.
#
'''setup'''


from setuptools import setup


with open("./LongDescription", 'r') as README_FILE:
    long_description = README_FILE.read()


setup(
    name='pspbar',
    version='0.0.0.0dev1',
    description="Prady's Swaybar in Python",
    license="GPLv3",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Pradyumna Paranjape',
    author_email='pradyparanjpe@rediffmail.com',
    url="https://github.com/pradyparanjpe",
    packages=['pspbar'],
    install_requires=['psutil'],
    scripts=['bin/pspbar',],
)
