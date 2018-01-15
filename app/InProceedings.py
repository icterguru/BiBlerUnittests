
import BibItems

class InProceedings(BibItems.BibItems):
    def setFields(self, bib):
        pass
        
    def __init__(self):
        super(InProceedings, self).__init__()
        self.editor = None
        self.series = None
        self.pages = None
        self.organization = None
        self.publisher = None
        self.address = None
        pass
    
