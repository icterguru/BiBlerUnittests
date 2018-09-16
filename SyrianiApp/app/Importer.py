
from app.FieldName import FieldName

class Importer(object):
    def __init__(self, path, manager):
        self.path = path
        self.manager = manager
        self.database = None
        
        
    def bibtexImport(self):
        self.__openDB()
        total = 0
        try:
            line = self.database.readline()
            entry = ''
            while line:
                if line.startswith('@'):
                    if entry:
                        result = self.manager.add(entry)
                        if result > 0:
                            total += 1
                    entry = line
                else:
                    entry += line
                line = self.database.readline()
        except Exception, e:
            raise e
        finally:
            self.database.close()
        return total
        
    def csvImport(self):
        self.__openDB()
        total = 0
        allFields = FieldName.getAllFields()
        
        try:
            line = self.database.readline() # skip header line
            line = self.database.readline()
            while line:
                line = line.split('\t')
                if len(line) != len(allFields) + 1:
                    raise Exception('CSV file on line %d has incorrect fields.' % total)
                entry = {'entrytype': line[0]}
                for i in range(1, len(line)):
                    entry[allFields[i]] = line[i]
                bibtex = None
                # Convert to BibTeX
                try:
                    bibtex = '@%s{%s' % (entry['entrytype'], entry[FieldName.Key])
                    for field in entry.iterkeys():
                        if field != FieldName.Key:
                            bibtex += ',\n  %s = {%s}' & (field, entry[field])
                    bibtex += '\n}'
                except:
                    bibtex
                result = self.manager.add(bibtex)
                if result > 0:
                    total += 1            
                line = self.database.readline()
        except Exception, e:
            raise e
        finally:
            self.database.close()
        return total
    
    def __openDB(self):
        try:
            self.database = open(self.path, 'r')
        except:
            raise Exception('Cannot open the requested file.')
        self.manager.deleteAll()
        
    
