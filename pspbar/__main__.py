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
'''Call module'''


from sys import exit as sysexit, modules
from datetime import datetime
from time import sleep
from .updatebar import main


if __name__ in ['__main__', 'pspbar.__main__']:
    if 'psutil' not in modules:
        while True:
            print('<span foreground=\\"#ff7f7fff\\"> Install psutil',
                  'meanwhile, falling back to basic:\t',
                  datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                  '</span>', flush=True)
            sleep(1)
    else:
        main()

# This will never happen
sysexit(0)
