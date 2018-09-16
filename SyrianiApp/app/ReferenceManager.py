
from EmptyEntry import EmptyEntry
from BibTeXParser import BibTeXParser
from FieldName import FieldName
from gui.app_interface import EntryListColumn

class ReferenceManager(object):
    def __init__(self):
        self.searchResult = list()
        self.entryList = list()
        pass
        
    def add(self, entryBibTeX):
        if entryBibTeX == None:
            entry = EmptyEntry()
            self.entryList.append(entry)
            return entry.getId()
        try:
            parser = BibTeXParser(entryBibTeX)
            entry = parser.parse()
            self.__setKey(entry)
            if entry.validate():
                self.entryList.append(entry)
                return entry.getId()
            else:
                return None
        except:
            return None
        
        
    def update(self, entryId, entryBibTeX):
        entry = self.getEntry(entryId)
        if entry == None:
            return False
        try:
            parser = BibTeXParser(entryBibTeX)
            new_entry = parser.parse()
            new_entry.setId(entryId)
            self.__setKey(new_entry)
            if new_entry.validate():
                # Overwrite the entry in entryList
                for i in xrange(self.getEntryCount()):
                    if self.entryList[i] == entry:
                        self.entryList[i] = new_entry
                        break
            else:
                return False
        except Exception, e:
            raise e
            return False
        return True
        
    def delete(self, entryId):
        entry = self.getEntry(entryId)
        if entry == None:
            return False
        self.entryList.remove(entry)
        return True
        
    def deleteAll(self):
        self.entryList = []
        self.searchResult = []
        
    def duplicate(self, entryId):
        entry = self.getEntry(entryId)
        if entry == None:
            return False
        return self.add(entry.toBibTeX())
        
    def search(self, query):
        try:
            self.searchResult = filter(lambda e: e.matches(query), self.entryList)
            return True
        except:
            return False
    
    def sort(self, field):
        try:
            if field == EntryListColumn.TYPE:
                self.entryList.sort(key=lambda e: e.getEntryType())
            elif field == EntryListColumn.ID:
                self.entryList.sort(key=lambda e: e.getId())
            else:
                self.entryList.sort(key=lambda e: e.getField(FieldName.fromEntryListColumn(field)))
            return True
        except:
            return False
    
    def getEntry(self, entryId):
        for e in self.entryList:
            if e.getId() == entryId:
                return e
        return None
        
    def iterEntryList(self):
        for entry in self.entryList:
            yield entry
        
    def getEntryCount(self):
        return len(self.entryList)
        
    def iterSearchResult(self):
        for entry in self.searchResult:
            yield entry
        
    def __setKey(self, entry):
        key = entry.generateKey()
        duplicateKeys = map(lambda e: e.getField(FieldName.Key),    # collect all keys that start with the same key
                            filter(lambda e: e.getId() != entry.getId() and e.getField(FieldName.Key).startswith(key), self.entryList))
        if len(duplicateKeys) > 27:
            raise Exception('Too many entries with the same key.')
        elif not duplicateKeys:
            entry.setField(FieldName.Key, key)
        else:
            suffix = ''
            for i in xrange(len(duplicateKeys) + 1):
                if key + suffix not in duplicateKeys:
                    entry.setField(FieldName.Key, key + suffix)
                    break
                suffix = chr(ord('a') + i)
