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
'''initialize package'''


from .classes import SBar, BarSeg
from .timer import TIME
from .cpu import CPU
from .ram import RAM
from .network import IP_ADDR, NETSPEED
from .temperature import TEMPERATURE
from .uname import OSNAME
from .battery import BATTERY

__all__ = [
    'SBar',
    'BarSeg',
    'TIME',
    'RAM',
    'CPU',
    'IP_ADDR',
    'NETSPEED',
    'TEMPERATURE',
    'OSNAME',
    'BATTERY',
]
