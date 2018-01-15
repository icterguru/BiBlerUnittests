
import BibItems

class RefManager(object):
    def AddRef(self, bib):
        print "Added"
        
    def AddUpdatedRef(self, count):
        pass
        
    def DeleteRef(self, entryid):
        pass
        
    def DeleteConf(self, entryId):
        pass
        
    def DuplicateRef(self, id):
        pass
        
    def ExpToFile(self, filepath, expstyle):
        pass
        
    def GetImpStyle(self, path, style):
        pass
        
    def getBibTex(self, id):
        pass
        
    def ImpFromFile(self, filepath, impstyle):
        pass
        
    def getRefCount(self):
        pass
        
    def GetRefType(self, bib):
        pass
        
    def GenerateKey(self, bib):
        pass
        
    def GenNewKey(self, string):
        pass
        
    def SearchRef(self, query):
        pass
        
    def SetExpStyle(self, path, style):
        pass
        
    def SelectEntry(self, entryId):
        pass
        
    def SetPrevStyle(self, style):
        pass
        
    def PreviewRef(self, id):
        pass
        
    def SortRef(self, field):
        pass
        
    def ReadFromFile(self, filepath, impstyle):
        pass
        
    def UpdateRef(self, id, bib):
        pass
        
    def WriteInFile(self, path, string):
        pass
        
    def __init__(self):
        self.RefList = list()
        self.bib = None
        self.refid = None
        self.refIdList = None
        self.refList = None
        pass
    
