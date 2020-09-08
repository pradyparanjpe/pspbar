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
'''Display OS name'''


from os import uname
from .classes import BarSeg


def osname(_=None) -> tuple:
    '''Create Linux release string'''
    return {'magnitude': f"{uname().release.split('.')[-2]}"}


OSNAME = BarSeg(symbol=chr(0x1f427), method=osname,
                ml_tag=['<span foreground="#7f9fffff">', '</span>'])
