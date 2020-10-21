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
'''Battery monitor and action segment'''


from typing import Dict
from subprocess import Popen
from psutil import sensors_battery
from .classes import BarSeg


EMOJIS = {
    "bat_100": '\uf240',
    "bat_75":  '\uf240',
    "bat_50":  '\uf242',
    "bat_25":  '\uf243',
    "bat_0":   '\uf244',

}


def _bat_act(conn, fill, mem) -> int:
    '''Emergency Actions'''
    if conn:
        if fill > 99 and mem < 5:
            mem += 1
            # Send only 5 notifications
            Popen(['notify-send', '-t', "5000", 'Battery_charged'])
    else:
        mem = 0
        if fill < 20:
            Popen(['notify-send', "-u", "critical", 'Battery Too Low'])
        elif fill < 10:
            Popen(['notify-send', "-u", "critical",
                   'Battery Too Low Suspending Session...'])
        elif fill < 5:
            Popen(['systemctl', 'suspend'])
    return mem


def battery(mem=None) -> Dict[str, str]:
    '''Create Battery summary string'''
    sym_ml = ['', '']
    bat_probe = sensors_battery()
    if not bat_probe:
        return {'symbol': EMOJIS['bat_0'], 'vis': False}
    bat_fill = bat_probe.percent
    bat_conn = bat_probe.power_plugged
    if bat_conn:
        sym_ml = ['<span foreground=\\"#7fffffff\\">', '</span>']
    # Action
    mem = _bat_act(conn=bat_conn, fill=bat_fill, mem=mem)
    # returns
    ml_tag = ['', '']
    if bat_fill >= 100:
        sym, val = EMOJIS['bat_100'], "100"
        ml_tag = ['<span foreground=\\"#7fffffff\\">', '</span>']
    elif bat_fill > 75:
        sym, val = EMOJIS['bat_75'], f"{bat_fill:.2f}"
        ml_tag = ['<span foreground=\\"#ffff7fff\\">', '</span>']
    elif bat_fill > 50:
        sym, val = EMOJIS['bat_50'], f"{bat_fill:.2f}"
        ml_tag = ['<span foreground=\\"#ffaf7fff\\">', '</span>']
    elif bat_fill > 25:
        sym, val = EMOJIS['bat_25'], f"{bat_fill:.2f}"
        ml_tag = ['<span foreground=\\"#ff7f7fff\\">', '</span>']
    else:
        sym, val = EMOJIS['bat_0'], f"{bat_fill:.2f}"
        ml_tag = ['<span foreground=\\"#ff5f5fff\\">', '</span>']
    sym = sym_ml[0] + sym + sym_ml[1]
    return {'symbol': sym, 'magnitude': val, 'mem': mem, 'ml_tag': ml_tag}


BATTERY = BarSeg(name="battery",
                 symbol=EMOJIS['bat_0'],
                 method=battery,
                 units="%",
                 mem=0)
