#!/usr/bin/python3
# -*- coding: latin-1 -*-

"""
Copyright (C) 2014 Technische Universitšt Berlin,
Fakultšt IV - Elektrotechnik und Informatik,
Fachgebiet Regelungssysteme,
Einsteinufer 17, D-10587 Berlin, Germany

This file is part of PaPI.

PaPI is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

PaPI is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with PaPI.  If not, see <http://www.gnu.org/licenses/>.

Contributors
Sven Knuth
"""
from papi.buffer.manager import Manager

__author__ = 'knuths'

import unittest

from multiprocessing import Array


class TestDBufferManager(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_array_size(self):

        queue_1 = Manager.get_array_size([[5, 100], [2, 1000]])
        self.assertEqual(len(queue_1), 25006)

        queue_2 = Manager.get_array_size([[2, 10]])
        self.assertEqual(len(queue_2), 203)

    def test_add_data(self):
        pass
        #emory_size = manager.get_array_size([[2, 10]])


        #bm = manager(shared_Arr)
