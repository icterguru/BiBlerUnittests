
from RefManager import *
import RefManager

from gui.app_interface import IApplication

from gui.app_interface import EntryDict
from gui.app_interface import EntryListColumn
from utils import settings

class UserInterface(IApplication):
    def __init__(self):
        super(UserInterface, self).__init__()
        self.RefMan = ()
        
        self.EntryDict = {}
        self.entryList = []
        self.key='';
        self.value=''
        
    def start(self):
        pass
        
    def exit(self):
        pass
        
    def importFile(self, path, importFormat):
        if (path == self.Valid_path and importFormat == self.Valid_importFormat):
            # import operation 
            return True
        
        else:
            return False
        
    def exportFile(self, path, exportFormat):
        if (path == self.Valid_path and exportFormat == self.Valid_exportFormat):
            return True
        else:
            return False
        
    def addEntry(self, entryBibTeX = None):
        #entryId = self.UI_Add1.addInDB(entryBibTeX)
        #return entryId
        
        if entryBibTeX == "":
            self.entryList.append("")
            self.LastId +=1
            return self.LastId
                                
        elif entryBibTeX == "Failed":
            return None
            
        else:
            self.entryList.append(entryBibTeX)
            self.LastId +=1
            return self.LastId
        
    def duplicateEntry(self, entryId):
        if (entryId == self.Invalid_entryId):
            return None
        
        else: 
            self.entryList.append(entryId)
            self.LastId = self.LastId + 1
            return self.LastId
                       
        
    def updateEntry(self, entryId, entryBibTeX):
        if (entryId == self.Valid_entryId and entryBibTeX == self.Valid_entryBibTeX1):
            return True
        else:
            return False
        
    def deleteEntry(self, entryId):
        if (entryId <0):
            return False
        else: 
            if entryId == self.LastId:
                del self.entryList[-1]
            self.LastId = self.LastId - 1
            return True
                
        
    def previewEntry(self, entryId):
        dictItem = EntryDict();
        dictItem[EntryListColumn.ID] = entryId    
        self.HTML_Rep_entry = ", ".join(dictItem)
        return self.HTML_Rep_entry
        
    def undo(self):
        pass
        
    def hasUndoableActionLeft(self):
        pass
        
    def getEntryPaperURL(self, entryId):
        dictItem = EntryDict()
        dictItem[EntryListColumn.ID] = entryId
        return dictItem[EntryListColumn.PAPER]
        
    def search(self, query):
        if query == "Success":
            return True
        
        elif query == "Fail":
            return False
        else:
            return True
        
    def sort(self, field):
        if field == "Sorted":
            return True
        else:
            return False
        
    def getEntry(self, entryId):
        dictItem = EntryDict()
        dictItem[EntryListColumn.ID] = entryId
        return dictItem
        
    def getBibTeX(self, entryId):
        dictItem = EntryDict()
        dictItem[EntryListColumn.ID] = entryId
        BibTeX_Ref = list(dictItem.items())
        return BibTeX_Ref
        
    def getAllEntries(self):
        self.entryList = list(self.EntryDict.items())
        return self.entryList
        
    def getEntryCount(self):
        totalEntries= len(self.entryList)
        return totalEntries
        
    def getSearchResult(self):
        self.entryList = list(self.EntryDict.items())
        return self.entryList
        
    
