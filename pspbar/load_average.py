#!/usr/bin/env python3
# -*- coding:utf-8; mode:python -*-
#
# Copyright 2020 Pradyumna Paranjape
# This file is part of pspbar.
#
# pspbar is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pspbar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pspbar.  If not, see <https://www.gnu.org/licenses/>.
#
'''LOAD monitor'''


from typing import Dict
from psutil import getloadavg, cpu_count
from .classes import BarSeg


def loadavg(_=None) -> Dict[str, str]:
    '''Create LOAD summary string'''
    ml_tag = ['', '']
    load_avg = list(map(lambda x: x * 100 / cpu_count(), getloadavg()))
    if load_avg[0] > 100:
        ml_tag = ['<span foreground=\\"#ff5f5fff\\">', '</span>']
    elif load_avg[0] > 80:
        ml_tag = ['<span foreground=\\"#ffaf7fff\\">', '</span>']
    elif load_avg[0] > 60:
        ml_tag = ['<span foreground=\\"#ffff5fff\\">', '</span>']
    else:
        return {'vis': False}
    value = "|".join((f'{load:.0f}' for load in load_avg))
    return {'magnitude': value, 'ml_tag': ml_tag}


LOAD = BarSeg(
    name="load",
    symbol=chr(0x1f3cb),
    method=loadavg,
    units="%"
)
