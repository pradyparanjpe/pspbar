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


from psutil import net_if_addrs, net_io_counters
from .classes import BarSeg


def ip_addr(_=None) -> tuple:
    '''Create IP ADDRESS string'''
    for ip_key in net_if_addrs().keys():
        if "wl" in ip_key:
            for sub_dev in list(net_if_addrs()[ip_key]):
                if sub_dev.netmask and sub_dev.broadcast:
                    addr = sub_dev.address
                    if addr.split(".")[:2] == ["192", "168"]:
                        return {'magnitude': ".".join(addr.split(".")[2:])}
                    return {'magnitude': sub_dev.address}
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
