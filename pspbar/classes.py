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
'''Classes'''


from time import sleep


class BarSeg():
    '''Segment object of the SBar'''
    def __init__(self, **kwargs) -> None:
        '''
        symbol: displayed on bar
        magnitude: the main thing
        units: suffixed to magnitude
        mem: initial (placeholder) memory to be added to buffer
        ml_tag: pango_tag to wrap around magnitude
        method: function that accepts a memory object returns
                (symbol, Magnitude, mem, ?Visible)

        Update Method Wrapper
        '''
        self.symbol = None
        self.method = None
        self.units = None
        self.vis = None
        self.mem = None
        self.ml_tag = None
        self.magnitude = None
        for key in ['magnitude', 'symbol', 'method',
                    'units', 'vis', 'mem', 'ml_tag']:
            setattr(self, key, kwargs.get(key, ''))
        self.method = self.method or (lambda: (None, None, None, True))
        if self.vis == '':
            self.vis = True
        if self.ml_tag == '':
            self.ml_tag = ['', '']

    def update(self, method=None) -> None:
        '''
        method: function that updates the segment
        kwargs: a dict object returned by METHOD, that may contain:
        symbol: to update
        magnitude: to update
        mem: to update
        ml_tag: pango tag to decorate
        vis: (bool) visibility

        Update magnitude and symbol
        '''
        if method:
            kwargs = method(self.mem)
        else:
            kwargs = self.method(self.mem)
        self.symbol = kwargs.get('symbol', self.symbol)
        self.magnitude = kwargs.get('magnitude', self.magnitude)
        self.vis = kwargs.get('vis', True)
        self.mem = kwargs.get('mem', self.mem)
        self.ml_tag = kwargs.get('ml_tag', self.ml_tag)


class SBar():
    '''Sway wrapper class'''
    def __init__(self):
        '''Initiate an empty bar'''
        self.bar_str = ''
        self.bar_segs = []
        self.quick_segs = []
        self.slow_segs = []
        self.static_segs = []

    def add_segs(self, segment: BarSeg,
                 interval: int = 1, position: int = None) -> None:
        '''
        interval: Interval of update. Numerical code:
        Beginning: 0,
        frequently: 1,
        intermittently: 2.
        position: Position of segment from edge
        kwargs: will be passed to BarSeg

        Add segment to bar
        '''
        self.bar_segs.insert(position, segment)

        if interval == 1:
            self.quick_segs.append(segment)
        elif interval == 2:
            self.slow_segs.append(segment)
        else:
            self.static_segs.append(segment)

    def _slow_tick(self) -> None:
        '''slow updating segments'''
        for seg in self.slow_segs:
            seg.update()

    def _quick_tick(self) -> None:
        '''fast updating widgets'''
        for seg in self.quick_segs:
            seg.update()

    def _static_vals(self) -> None:
        '''static segments'''
        for seg in self.static_segs:
            seg.update()

    def _update_str(self, sep='|') -> None:
        '''Update bar string'''
        sep = ","
        self.bar_str = f' {sep} '.join(
            reversed(
                ['{"full_text":"' + f'\
{seg.symbol} \
{seg.ml_tag[0]} {seg.magnitude} {seg.ml_tag[1]}\
{seg.units}' + '", "markup":"pango"}'
                 for seg in filter(lambda x: x.vis, self.bar_segs)]
            )
        )
        self.bar_str = f", [{self.bar_str}]"

    def loop(self, period: int = 1, multi: int = 1) -> None:
        '''
        period: Period between two updates in seconds.

        Loop update
        float is discouraged
        '''
        self._static_vals()
        long_per = 0
        while True:
            self._quick_tick()
            if not long_per:
                self._slow_tick()
            self._update_str(" ")
            print(self.bar_str, flush=True)
            long_per = (long_per + period) % multi
            sleep(period)
