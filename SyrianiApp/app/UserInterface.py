'''
Created on Jan 13, 2014
@author: Eugene Syriani
@version: 0.2.5

This module represents the interface to the L{gui} package.
'''

from gui.app_interface import IApplication
from ReferenceManager import ReferenceManager
from Importer import Importer
from Exporter import Exporter
from FieldName import FieldName
from utils import settings

prefs = settings.Preferences()

class UserInterface(IApplication):
    def __init__(self):
        super(UserInterface, self).__init__()
        self.referenceManager = ReferenceManager()
        pass
        
    def start(self):
        pass
        
    def exit(self):
        pass
        
    def importFile(self, path, importFormat):
        total = 0
        importer = Importer(path, self.referenceManager)
        if importFormat == settings.ImportFormat.BIBTEX:
            total = importer.bibtexImport()
        elif importFormat == settings.ImportFormat.CSV:
            total = importer.csvImport()
        return total > 0
        
    def exportFile(self, path, exportFormat):
        total = 0
        exporter = Exporter(path, self.referenceManager.iterEntryList())
        if exportFormat == settings.ExportFormat.BIBTEX:
            total = exporter.bibtexExport()
        elif exportFormat == settings.ExportFormat.CSV:
            total = exporter.csvExport()
        elif exportFormat == settings.ExportFormat.HTML:
            if prefs.bibStyle == settings.BibStyle.ACM:
                total = exporter.htmlACMExport()
            elif prefs.bibStyle == settings.BibStyle.IEEE:
                total = exporter.htmlIEEETransExport()
        return total > 0
        
    def addEntry(self, entryBibTeX):
        return self.referenceManager.add(entryBibTeX)
        
    def duplicateEntry(self, entryId):
        return self.referenceManager.duplicate(entryId)
        
    def updateEntry(self, entryId, entryBibTeX):
        return self.referenceManager.update(entryId, entryBibTeX)
        
    def deleteEntry(self, entryId):
        return self.referenceManager.delete(entryId)
        
    def previewEntry(self, entryId):
        entry = self.referenceManager.getEntry(entryId)
        if prefs.bibStyle == settings.BibStyle.ACM:
            return entry.toHTMLACM()
        elif prefs.bibStyle == settings.BibStyle.IEEE:
            return entry.toHTMLIEEETrans()
        
    def getEntryPaperURL(self, entryId):
        return self.referenceManager.getEntry(entryId).getField(FieldName.Paper)
        
    def search(self, query):
        return self.referenceManager.search(query)
        
    def sort(self, field):
        return self.referenceManager.sort(field) 
        
    def getEntry(self, entryId):
        return self.referenceManager.getEntry(entryId).toEntryDict()
        
    def getBibTeX(self, entryId):
        return self.referenceManager.getEntry(entryId).toBibTeX()
        
    def getAllEntries(self):
        entries = []
        for entry in self.referenceManager.iterEntryList():
            entries.append(entry.toEntryDict())
        return entries
        
    def getEntryCount(self):
        return self.referenceManager.getEntryCount()
        
    def getSearchResult(self):
        entries = []
        for entry in self.referenceManager.iterSearchResult():
            entries.append(entry.toEntryDict())
        return entries
        
    
