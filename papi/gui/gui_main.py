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

__author__ = 'knuths'

import sys
import time

from PySide.QtGui import QMainWindow, QApplication

import pyqtgraph as pg
from pyqtgraph import QtGui, QtCore

# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=False)

from papi.ui.gui.main import Ui_MainGUI
from papi.gui.manager import Manager
from papi.PapiEvent import PapiEvent
from papi.data.DGui import DGui
from yapsy.PluginManager import PluginManager
from papi.ConsoleLog import ConsoleLog


class GUI(QMainWindow, Ui_MainGUI):

    def __init__(self, core_queue, gui_queue,gui_id, parent=None):
        super(GUI, self).__init__(parent)
        self.setupUi(self)

        self.create_actions()

        self.manager_visual = Manager('visual')
        self.manager_io = Manager('io')
        self.manager_parameter = Manager('parameter')

        self.setWindowTitle('PaPI')

        self.core_queue = core_queue
        self.gui_queue = gui_queue

        self.gui_id = gui_id

        self.count = 0

        QtCore.QTimer.singleShot(40,self.gui_working)

        self.process_event = {  'new_data': self.process_new_data_event,
                                'close_programm': self.process_close_program_event,
                                'check_alive_status': self.process_check_alive_status,
                                'create_plugin':self.process_create_plugin
        }

        self.gui_data = DGui()

        self.log = ConsoleLog(2,'Gui-Process: ')

        self.plugin_manager = PluginManager()
        self.plugin_manager.setPluginPlaces(["plugin"])



    def dbg(self):
        print("Action")

    def create_actions(self):
        self.actionM_License.triggered.connect(self.menu_license)
        self.actionM_Quit.triggered.connect(self.menu_quit)

        self.actionAP_Visual.triggered.connect(self.ap_visual)
        self.actionAP_IO.triggered.connect(self.ap_io)
        self.actionAP_Parameter.triggered.connect(self.ap_parameter)

        self.actionRP_IO.triggered.connect(self.rp_io)
        self.actionRP_Visual.triggered.connect(self.rp_visual)

        self.stefans_button.clicked.connect(self.stefan)

    def menu_license(self):
        pass

    def menu_quit(self):
        self.close()
        pass

    def ap_visual(self):
        self.manager_visual.show()

        pass

    def ap_io(self):
        self.manager_io.show()
        pass

    def ap_parameter(self):
        self.manager_parameter.show()
        pass

    def rp_visual(self):
        pass

    def rp_io(self):
        pass

    def closeEvent(self, *args, **kwargs):
        event = PapiEvent(self.gui_id, 0, 'instr_event','close_program','Reason')
        self.core_queue.put(event)
        self.manager_visual.close()
        self.manager_parameter.close()
        self.manager_io.close()
        self.close()

    def stefan(self):
        self.count += 1

        event = PapiEvent(self.gui_id, 0, 'instr_event','create_plugin','Sinus')
        self.core_queue.put(event)
        event = PapiEvent(self.gui_id, 0, 'instr_event','create_plugin','Plot')
        self.core_queue.put(event)
        event = PapiEvent(3,0,'instr_event','subscribe',2)
        self.core_queue.put(event)

        if self.count <= 0:
            event = PapiEvent(self.gui_id, 0, 'instr_event','create_plugin','Sinus')
            self.core_queue.put(event)
        if (self.count > 100):
            event = PapiEvent(self.gui_id, 2, 'instr_event','stop_plugin','')
            self.core_queue.put(event)


    def gui_working(self):
        """
         :type event: PapiEvent
         :type dplugin: DPlugin
        """
        try:
            event = self.gui_queue.get_nowait()
            op = event.get_event_operation()
            self.log.print(2,'Event: '+ op)
            self.process_event[op](event)


            # TODO: DGui strucutre und fuellen dieser Struktur vom Core aus
            # TODO: event verteilung und reagieren auf events
            # TODO: ausfuehren von Fuktionen aus den plugins "execute"
        except:
            pass

        finally:
            QtCore.QTimer.singleShot(40,self.gui_working)



    def process_new_data_event(self,event):
        """
         :param event: event to process
         :type event: PapiEvent
         :type dplugin: DPlugin
        """

        dID = event.get_destinatioID()
        dplugin = self.gui_data.get_dplugin_by_id(dID)
        if dplugin != None:
            dplugin.plugin.plugin_object.execute(event.get_optional_parameter())
            return 1
        else:
            self.log.print(1,'new_data, Plugin with id  '+str(dID)+'  does not exist in DGui')
            return -1


    def process_create_plugin(self,event):
        """
         :param event: event to process
         :type event: PapiEvent
         :type dplugin: DPlugin
        """
        optPar = event.get_optional_parameter()
        id = optPar[1]
        plugin_identifier = optPar[0]
        uname = optPar[2]

        array = None

        self.plugin_manager.collectPlugins()
        plugin = self.plugin_manager.getPluginByName(plugin_identifier)

        if plugin == None:
            self.log.print(1,'create_plugin, Plugin with Name  '+plugin_identifier+'  does not exist in file system')
            return -1



        dplugin =self.gui_data.add_plugin(None,None,False,self.gui_queue,array,plugin,id)
        dplugin.uname = uname
        buffer = 1

        dplugin.plugin.plugin_object.init_plugin(self.core_queue, self.gui_queue, array,buffer,dplugin.id)
        self.log.print(2,'create_plugin, Plugin with name  '+str(dplugin.plugin.name)+'  was started')

    def process_close_program_event(self,event):
        """
         :param event: event to process
         :type event: PapiEvent
         :type dplugin: DPlugin
        """
        pass


    def process_check_alive_status(self,event):
        """
         :param event: event to process
         :type event: PapiEvent
         :type dplugin: DPlugin
        """
        pass




def startGUI(CoreQueue, GUIQueue,gui_id):
    app = QApplication(sys.argv)
#    mw = QtGui.QMainWindow
    gui = GUI(CoreQueue, GUIQueue,gui_id)
    gui.show()
    app.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
#    mw = QtGui.QMainWindow
    frame = GUI(None,None,None)
    frame.show()
    app.exec_()
