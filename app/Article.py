
import BibItems

class Article(BibItems.BibItems):
    def setFields(self, bib):
        pass
        
    def __init__(self):
        super(Article, self).__init__()
        self.volume = None
        self.number = None
        self.pages = None
        self.journal = None
        pass
    
