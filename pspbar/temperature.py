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
'''Temperature monitoring and acting segment'''


from psutil import sensors_temperatures
from .classes import BarSeg


EMOJIS = {
    "fire":    chr(0x1f525),
    "temp_100": '\uf2c7',
    "temp_75":  '\uf2c8',
    "temp_50":  '\uf2c9',
    "temp_25":  '\uf2ca',
    "temp_0":   '\uf2cb',
}


def heat_mon(_=None) -> tuple:
    '''Create Temperature summary string'''
    ml_tag = ['', '']
    heat = sensors_temperatures()['coretemp'][0].current
    if heat > 80:
        sym, val = EMOJIS['fire'], f"{heat:.0f}"
        ml_tag = ['<span foreground=\\"#ff5f5fff\\">', '</span>']
    elif heat > 70:
        sym, val = EMOJIS['temp_100'], f"{heat:.0f}"
        ml_tag = ['<span foreground=\\"#ffaf7fff\\">', '</span>']
    elif heat > 60:
        sym, val = EMOJIS['temp_75'], f"{heat:.0f}"
        ml_tag = ['<span foreground=\\"#ffff5fff\\">', '</span>']
    elif heat > 50:
        sym, val = EMOJIS['temp_50'], f"{heat:.0f}"
    elif heat > 40:
        sym, val = EMOJIS['temp_25'], f"{heat:.0f}"
    else:
        sym, val = EMOJIS['temp_0'], f"{heat:.0f}"
    return {'symbol': sym, 'magnitude': val, 'ml_tag': ml_tag}


TEMPERATURE = BarSeg(name="temperature",
                     symbol=EMOJIS['fire'],
                     method=heat_mon,
                     units='\u2103') 
