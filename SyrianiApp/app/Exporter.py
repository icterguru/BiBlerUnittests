
from app.FieldName import FieldName

class Exporter(object):
    def __init__(self, path, entries):
        self.path = path
        self.entries = entries
        self.database = None
        
    def bibtexExport(self):
        return self.__export(lambda e: e.toBibTeX())
        
    def csvExport(self):
        return self.__export(lambda e: e.toCSV())
        
    def htmlIEEETransExport(self):
        return self.__export(lambda e: e.toHTMLIEEETrans())
        
    def htmlACMExport(self):
        return self.__export(lambda e: e.toHTMLACM())
    
    def __export(self, exporter):
        try:
            self.database = open(self.path, 'w')
        except:
            raise Exception('Cannot open the requested file.')
        total = 0
        try:
            allFields = FieldName.getAllFields()
            self.database.write('entrytype\t' + '\t'.join(allFields) + '\n')    # headers
            for entry in self.entries:
                bibtex = exporter(entry)
                self.database.write(bibtex + '\n')
                total += 1
        except Exception, e:
            raise e
        finally:
            self.database.close()
        return total
        
    
