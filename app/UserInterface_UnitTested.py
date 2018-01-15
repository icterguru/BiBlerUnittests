'''
Created on Jan 13, 2014
@author: Eugene Syriani
@version: 0.2.5

This module represents the interface to the L{gui} package.
'''

from gui.app_interface import IApplication

from gui.app_interface import EntryDict
from gui.app_interface import EntryListColumn
from utils import settings


prefs = settings.Preferences()


            
class UserInterface(IApplication):
    """
    This class serves as the external API of the core behavior of BiBler.
    
    TODO: Assignment 1: Implement the IApplication interface such that it minimally satisfies your unit tests.
    
    TODO: Assignment 2: This class must be automatically generated.
    """
    #TODO: Assignment 1: Implement the IApplication interface such that it minimally satisfies the tests.
    
    
    
    def __init__(self):
        
        self.EntryDict = {}
        
        
        self.entryList = []
        
        self.key='';
        self.value=''

        

    
 
        
    def start(self): 
        pass
    
    
    def exit(self): 
        pass
    
 
 
 

    def importFile(self, path, importFormat):
        """
        Import a list of entries from a file in a given format.
        @type path: L{str}
        @param path: The path to a file.
        @type importFormat: L{utils.settings.ImportFormat}
        @param importFormat: The format of the file.
        @rtype: L{bool}
        @return: C{True} if succeeded, C{False} otherwise.
        """
        
        if (path == self.Valid_path and importFormat == self.Valid_importFormat):
            # import operation 
            return True
      
        else:    
            return False
     
    def exportFile(self, path, exportFormat):
        """
        Export the list of entries to a file in a given format.
        @type path: L{str}
        @param path: The path to a file.
        @type exportFormat: L{utils.settings.ExportFormat}
        @param exportFormat: The format of the file.
        @rtype: L{bool}
        @return: C{True} if succeeded, C{False} otherwise.
        """
        if (path == self.Valid_path and exportFormat == self.Valid_exportFormat):
            # export operation
            return True
        
        else:    
            return False
    
    
    def addEntry(self, entryBibTeX=None):
        """
        Add a new entry. If C{entryBibTeX==None}, an empty entry is created.
        @type entryBibTeX: L{str}
        @param entryBibTeX: The BibTeX reference of the entry. 
        @rtype: L{int}
        @return: The I{id} of the new entry. C{None} is returned if failed.
        """
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
        """
        Create a copy of an existing entry.
        @type entryId: L{int}
        @param entryId: The I{id} of the entry to copy.
        @rtype: L{int}
        @return: The I{id} of the new entry. C{None} is returned if failed.
        """
        
        if (entryId == self.Invalid_entryId):
            return None
        else: 
            
            self.entryList.append(entryId)
        
        self.LastId = self.LastId + 1
        return self.LastId
               

    
    def updateEntry(self, entryId, entryBibTeX):
        """
        Update an entry with a new BibTeX reference.
        @type entryId: L{int}
        @param entryId: The I{id} of the entry to update. 
        @type entryBibTeX: L{str}
        @param entryBibTeX: The BibTeX reference. 
        @rtype: L{bool}
        @return: C{True} if succeeded, C{False} otherwise.
        """
        ##
        if (entryId == self.Valid_entryId and entryBibTeX == self.Valid_entryBibTeX1):
                    
            return True
        
        else:    
            return False
     
        
        
    def deleteEntry(self, entryId):
        """
        Delete an entry.
        @type entryId: L{int}
        @param entryId: The I{id} of the entry to delete. 
        @rtype: L{bool}
        @return: C{True} if succeeded, C{False} otherwise.
        """
         
        if (entryId <0):
               
            return False
      
        else: 
            if entryId == self.LastId:
                del self.entryList[-1]
            
            self.LastId = self.LastId - 1
            return True
              
     
    def previewEntry(self, entryId):
        
        """
        Convert an entry into its HTML representation following the bibliography style specified in L{utils.settings.Preferences}.
        @type entryId: L{int}
        @param entryId: The I{id} of the entry to preview. 
        @rtype: L{str}
        @return: The HTML representation of the entry.
        """
        
        dictItem = EntryDict();
        dictItem[EntryListColumn.ID] = entryId    
        self.HTML_Rep_entry = ", ".join(dictItem)
        return self.HTML_Rep_entry
           
        
 
    
    def getEntryPaperURL(self, entryId):
        """ 
        Get the URL of the paper of the selected entry.
        @type entryId: L{int}
        @param entryId: The I{id} of the entry. 
        @rtype: L{str}
        @return: The URL (or path) to the file.
        """
        #raise NotImplementedError()
          
        dictItem = EntryDict()
        dictItem[EntryListColumn.ID] = entryId    
        return dictItem[EntryListColumn.PAPER]

    
    def search(self, query):
        """
        Search for entries that satisfy the query provided.
        @type query: L{str}
        @param query: The query to match.
        @rtype: L{bool}
        @return: C{True} if succeeded, C{False} otherwise.
        @note: C{True} is returned even if no results were found.
        """
        
        
        if query == "Success":
            return True
        
        elif query == "Fail":
            return False
                
        else: 
            return True
               
                           

    
    def sort(self, field):
        """
        Inplace sort of in alphabetically increasing order all entries with respect to a field.
        @type field: L{EntryListColumn}
        @param field: The field to sort on.
        @rtype: L{bool}
        @return: C{True} if succeeded, C{False} otherwise.
        """
         
        if field == "Sorted":
            return True
        
        else:
            return False
                
         
    def getEntry(self, entryId):
        """
        Convert an entry into an L{EntryDict}.
        @type entryId: L{int}
        @param entryId: The I{id} of the entry. 
        @rtype: L{EntryDict}
        @return: The entry.
        """
        #raise NotImplementedError()
        
        dictItem = EntryDict();
        dictItem[EntryListColumn.ID] = entryId    
        return dictItem
        
      
    def getBibTeX(self, entryId):
        """
        Convert an entry into its BibTeX reference.
        @type entryId: L{int}
        @param entryId: The I{id} of the entry. 
        @rtype: L{str}
        @return: The BibTeX reference.
        """
                
        dictItem = EntryDict()
        dictItem[EntryListColumn.ID] = entryId
        BibTeX_Ref = list(dictItem.items())    
        return BibTeX_Ref
        
   
    def getAllEntries(self):
        """
        Get the list of all entries converted into L{EntryDict}.
        @rtype: L{list}
        @return: The list of entries.
        """
        #self.entryList = list(self.entryDict.items())
        
        self.entryList = list(self.EntryDict.items())

        return self.entryList
    
    
    def getEntryCount(self):
        """
        Get the total number of entries.
        @rtype: L{int}
        @return: The total.
        """
        totalEntries= len(self.entryList)
        return totalEntries


    def getSearchResult(self):
        """
        Get the list of entries filtered by the search.
        @rtype: L{EntryDict}
        @return: The list of entries.
        """
        
        self.entryList = list(self.EntryDict.items())

        return self.entryList
