
import BibItems

class Book(BibItems.BibItems):
    def setFields(self, bib):
        pass
        
    def __init__(self):
        super(Book, self).__init__()
        self.publisher = None
        self.volume = None
        self.series = None
        self.address = None
        self.edition = None
        self.editor = None
        pass
    
