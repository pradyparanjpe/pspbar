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
'''RAM monitoring segment'''


from psutil import virtual_memory
from .classes import BarSeg


def ram_use(_=None) -> tuple:
    '''Create RAM summary string'''
    ram_fill = virtual_memory().percent
    ml_tag = ['', '']
    if ram_fill > 80:
        ml_tag = ['<span foreground="#ff5f5fff">', '</span>']
    elif ram_fill > 60:
        ml_tag = ['<span foreground="#ffff5fff">', '</span>']
    return {'magnitude': f"{ram_fill:.0f}", 'ml_tag': ml_tag}


RAM = BarSeg(symbol='\uf233', method=ram_use, units="%")
