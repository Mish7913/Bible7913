#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright: 2017 Mish7913 <mish7913@gmail.com>
#  License:   GNU General Public License v2 or later

import os, sys, codecs;
path = os.path.dirname(os.path.abspath(__file__));
sys.path.insert(0, path + '/dp');
about = 'Словарь Стронга, русский перевод.';
from ru_strong_data import get_strong;
