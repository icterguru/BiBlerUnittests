'''
Created on Jan 13, 2014
@author: Eugene Syriani
@version: 0.2.5

This is the main BiBler module.
Execute this module from the command line to start the application.

@note: It assumes that the L{app} package has a L{statechart.BiBler_Statechart} class
and a L{UserInterface.UserInterface} class that implements L{gui.app_interface.IApplication}.

G{packagetree app, gui, utils}
'''

import wx
from gui.gui import MainWindow 
from gui.controller import Controller
from app.statechart import BiBler_Statechart
from app.UserInterface import UserInterface

if __name__ == '__main__':
    app = wx.App(False)
    controller = Controller()
    controller.bindGUI(MainWindow(controller))
    controller.bindSC(BiBler_Statechart())
    controller.bindApp(UserInterface())
    controller.start()
    app.MainLoop()