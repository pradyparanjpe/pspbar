#!/usr/bin/env python3
# -*- coding:utf-8; mode:python -*-
#
# Copyright 2020 Pradyumna Paranjape
# This file is part of pspbar.
#
# pspbar is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or # (at your option) any later version. #
# pspbar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pspbar.  If not, see <https://www.gnu.org/licenses/>.
#
'''
sway bar output
'''

from sys import exit as sysexit
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from warnings import filterwarnings
from .classes import SBar
from .timer import TIME
from .cpu import CPU
from .ram import RAM
from .network import IP_ADDR, NETSPEED
from .temperature import TEMPERATURE
from .uname import OSNAME
from .battery import BATTERY


def parse_cli() -> tuple:
    '''Parse CLI to receive update loop period'''
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("period", type=int, default=1, nargs='?',
                        help="period between successive updates in seconds")
    parser.add_argument("-s", "--stats", type=int, default=1,
                        help="multple of 'period' to update other stats")
    args = parser.parse_args()
    period = args.period or 1
    multi = args.stats or 1
    return period, multi


def main():
    '''Main Routine'''
    filterwarnings('ignore')
    period, multi = parse_cli()
    topbar = SBar()
    NETSPEED.mem = [period * multi, 0, 0]
    topbar.add_segs(segment=TIME, position=0, interval=1)
    topbar.add_segs(segment=BATTERY, position=1, interval=2)
    topbar.add_segs(segment=CPU, position=2, interval=1)
    topbar.add_segs(segment=TEMPERATURE, position=3, interval=2)
    topbar.add_segs(segment=RAM, position=4, interval=1)
    topbar.add_segs(segment=IP_ADDR, position=5, interval=0)
    topbar.add_segs(segment=NETSPEED, position=6, interval=2)
    topbar.add_segs(segment=OSNAME, position=7, interval=0)
    print('{ "version": 1, "click_events": true }', "[", "[]", sep="\n")
    topbar.loop(period=period, multi=multi)


if __name__ == "__main__":
    main()

    # This will never happen
    sysexit(0)
