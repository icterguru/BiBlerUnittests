
import Entry
from gui.app_interface import EntryListColumn
from app.FieldName import FieldName

class EmptyEntry(Entry.Entry):
        
    def __init__(self):
        super(EmptyEntry, self).__init__()
        for column in EntryListColumn.list():
            if column != EntryListColumn.ID and column != EntryListColumn.TYPE:
                self.optionalFields[FieldName.fromEntryListColumn(column)] = ''
    
    def validate(self):
        # No field should exist
        return not self.requiredFields.keys() and not self.optionalFields.keys()
        
    def toBibTeX(self):
        return ''
        
    def toHTMLIEEETrans(self):
        return ''
        
    def toHTMLACM(self):
        return ''
    
    def getEntryType(self):
        return ''
    
