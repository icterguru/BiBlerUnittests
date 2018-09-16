'''
Created on Jan 13, 2014
@author: Eugene Syriani
@version: 0.2.5

This module is responsible for managing all resources of BiBler.
'''

import utils
import os

class ResourceManager(object):
    """
    Give access to the resource files.
    @sort: _*, get*
    """
    __metaclass__ = utils.Singleton
    def __init__(self):
        self.pdfImagePath = 'utils/resources/pdf.png'
        self.aboutHTMLPath = 'utils/resources/about.html'
        self.usermanualHTMLPath = 'utils/resources/manual.html'
        self.iconPath = 'utils/resources/bibler.ico'
    
    def getAboutHTML(self):
        """
        Get the path to the web page for the L{AboutBox<gui.gui.AboutBox>}.
        """
        return self.__getPath(self.aboutHTMLPath)
    
    def getUserManualHTML(self):
        """
        Get the path to the web page for the L{UserManualWindow<gui.gui.UserManualWindow>}.
        """
        return self.__getPath(self.usermanualHTMLPath)
    
    def getPaperImagePath(self):
        """
        Get the path to image for entries with papers.
        """
        return self.__getPath(self.pdfImagePath)
    
    def getIconPath(self):
        """
        Get the path to the icon of BiBler.
        """
        return self.__getPath(self.iconPath)
    
    def __getPath(self, path):
        """
        Validates that a path exists.
        @type path: L{str}
        @param path: The path.
        @rtype: L{str}
        @return: The validated path.
        @raise Exception: if the resource file was not found.
        """
        if os.path.exists(path):
            return path
        else:
            raise Exception('Resource file ' + path + ' is missing.')
