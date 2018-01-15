
import BibItems

class TechReport(BibItems.BibItems):
    def setFields(self, bib):
        pass
        
    def __init__(self):
        super(TechReport, self).__init__()
        self.type = None
        self.number = None
        self.address = None
        self.institution = None
        pass
    
