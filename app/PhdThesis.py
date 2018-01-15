
import BibItems

class PhdThesis(BibItems.BibItems):
    def setFields(self, bib):
        pass
        
    def __init__(self):
        super(PhdThesis, self).__init__()
        self.address = None
        self.year = None
        pass
    
