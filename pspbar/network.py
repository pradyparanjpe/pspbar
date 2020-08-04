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
'''(WIFI)Internet-monitoring segments'''


from os.path import join as joinpath
from os.path import dirname as pathdirname
from subprocess import Popen, PIPE
from psutil import net_io_counters
from .classes import BarSeg


NETCHECK = joinpath(pathdirname(__file__), 'shell_dep',
                    'netcheck.sh')


def ip_addr(_=None) -> tuple:
    '''Create IP ADDRESS string'''
    color = 0x777777
    stdout, stderr = Popen(
        ['bash', NETCHECK], stdout=PIPE, stderr=PIPE
    ).communicate()
    stdout = stdout.decode("utf-8")
    print("NET_STATUS:", stdout, stderr)
    if not stderr:
        addr = stdout.split("\t")[0]
        net_type = int(stdout.split("\t")[2])
        if net_type & 8:
            # internet connected
            color += 0x008800
        elif net_type & 4:
            # intranet connected
            color += 0x888800
        else:
            color += 0x880000
        if net_type & 2:
            # On home network
            color += 0x000088
        elif net_type & 1:
            color += 0x000044
        ml_tag = [f'<span foreground="#{hex(color)[2:]}">', '</span>']
        if addr.split(".")[:2] == ["192", "168"]:
            return {'magnitude': ".".join(addr.split(".")[2:]),
                    'ml_tag': ml_tag}
        return {'magnitude': addr}
    return {'vis': False}


def netspeed(mem=None) -> tuple:
    '''Total internet Speed'''
    net_stats = net_io_counters()
    if not net_stats:
        return {'mem': mem}
    down_l = net_stats.bytes_recv / 1048576
    up_l = net_stats.bytes_sent / 1048576
    diff = (down_l - mem[1])/mem[0], (up_l - mem[2])/mem[0]
    return {'magnitude': f"{diff[0]:.2f}/{diff[1]:.2f}",
            'mem': [mem[0], down_l, up_l]}


IP_ADDR = BarSeg(symbol=chr(0x1f4f6), method=ip_addr, units="")
NETSPEED = BarSeg(symbol='\u21f5\u25BC', method=netspeed, units='\u25B2MB/s')
