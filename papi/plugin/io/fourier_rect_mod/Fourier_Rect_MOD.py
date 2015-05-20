#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Copyright (C) 2014 Technische Universität Berlin,
Fakultät IV - Elektrotechnik und Informatik,
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

__author__ = 'knuths'

from papi.plugin.base_classes.iop_base import iop_base
from papi.data.DPlugin import DBlock
from papi.data.DParameter import DParameter

import threading

import time
import numpy
import os

import socket
import pickle


class Fourier_Rect_MOD(iop_base):
    max_approx = 20
    amax = 20
    def start_init(self, config=None):
        self.t = 0
        self.amax = Fourier_Rect_MOD.amax
        self.amplitude = 1
        self.max_approx = Fourier_Rect_MOD.max_approx
        self.freq = 1
        self.vec = numpy.ones(self.amax* ( self.max_approx + 1) )

        print(['Fourier: process id: ',os.getpid()] )


        self.HOST = "130.149.155.73"
        self.PORT = 9999
        # SOCK_DGRAM is the socket type to use for UDP sockets
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setblocking(0)


        names = ['t']
        for i in range(1,self.max_approx):
            names.append('rect'+str(i))

        self.block1 = DBlock(None,300,10,'Rect1',names)
        self.send_new_block_list([self.block1])

        self.set_event_trigger_mode(True)

        thread = threading.Thread(target=self.thread_execute, args=(self.HOST,self.PORT) )
        thread.start()

        return True

    def pause(self):
        pass

    def resume(self):
        pass

    def thread_execute(self,host,port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #self.sock.setblocking(0)
        vec = numpy.zeros( (self.max_approx,  (self.amax) ))

        while True:
            self.sock.sendto(b'GET', (self.HOST, self.PORT) )

            try:
                received = self.sock.recv(60000)
            except socket.error:
                pass
            else:
                data = pickle.loads(received)

                for i in range(self.max_approx):
                    vec[i, 0:self.amax] = data[i*self.amax:(i+1)*self.amax]

                self.send_new_data(vec[0],vec[1:] ,'Rect1')

            time.sleep(0.001*self.amax )


    def execute(self, Data=None, block_name = None):
        print("EXECUTE FUNC")
        pass

    def set_parameter(self, name, value):
        pass

    def quit(self):
        print('Fourier_Rect: will quit')

    def plugin_meta_updated(self):
        pass

    def get_plugin_configuration(self):
        return {}