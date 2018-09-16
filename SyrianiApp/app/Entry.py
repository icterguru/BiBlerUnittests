
from gui.app_interface import EntryDict, EntryListColumn
from FieldName import FieldName

class Entry(object):
    lastID = 0
    def __init__(self):
        self.__id = Entry.lastID
        self.requiredFields = dict()
        self.optionalFields = dict()
        Entry.lastID += 1
        
    def getId(self):
        return self.__id
        
    def setId(self, _id):
        self.__id = _id
        
    def getField(self, field):
        if field in self.requiredFields:
            return self.requiredFields[field]
        elif field in self.optionalFields:
            return self.optionalFields[field]
        else:
            raise Exception('Invalid field requested.')
        
    def setField(self, field, value):
        if field in self.requiredFields:
            self.requiredFields[field] = value
        elif field in self.optionalFields:
            self.optionalFields[field] = value
    
    def generateKey(self):
        # First author's last name (no {}, no spaces) concatenated with year
        return self.getFormattedField(FieldName.Author).split(',')[0].replace(' ', '') + self.getField(FieldName.Year)
        
    def validate(self):
        # Check that all required fields are not empty
        for field in self.requiredFields:
            if not self.requiredFields[field]:
                return False
        return True
        
    def matches(self, query):
        for field in self.requiredFields.iterkeys():
            if query in self.getFormattedField(field):
                return True
        for field in self.optionalFields.iterkeys():
            if query in self.getFormattedField(field):
                return True
        return False
    
    def toEntryDict(self):
        e = EntryDict()
        e[EntryListColumn.ID] = self.getId()
        e[EntryListColumn.TYPE] = self.getEntryType()
        for field in self.requiredFields:
            col = FieldName.toEntryListColumn(field)
            e[col] = self.requiredFields[field]
        for field in self.optionalFields:
            col = FieldName.toEntryListColumn(field)
            e[col] = self.optionalFields[field]
        return e
        
    def toBibTeX(self):
        #@TYPE{KEY,
        #  FIELD1 = {VALUE1},
        #  FIELD2 = {VALUE2}
        #}
        def bibify(fieldList):
            bibtex = ''
            for field in fieldList:
                if field == FieldName.Key:
                    continue
                value = fieldList[field]
                # This part is to put {} around capital letters if they aren't already
                v = ''
                for i in xrange(len(value)):
                    if value[i].isupper():
                        if 0 < i < len(value) - 1 and value[i-1] != '{' and value[i+1] != '}':
                            v += '{%s}' % value[i]
                    else:
                        v += value[i]
                bibtex += ',\n  %s = {%s}' % (field, value)
            return bibtex
        try:
            bibtex = '@%s{%s' % (self.getEntryType(), self.getField(FieldName.Key))
            bibtex +=  bibify(self.requiredFields)
            bibtex +=  bibify(self.optionalFields)
            bibtex += '\n}'
            return bibtex
        except Exception, e:
            raise e
            return ''
        
    def toCSV(self):
        #"VALUE1"\t"VALUE2"
        # Where the order is determined by FieldName.getAllFields()
        try:
            csv = self.getEntryType()   # the first column is the entrytype
            for field in FieldName.getAllFields():
                csv += '\t'
                try:
                    csv += '"' + self.getField(field) + '"'
                except:
                    continue    # the field is not in this entrytype
            return csv
        except:
            return ''
        
    def toHTMLIEEETrans(self):
        pass
        
    def toHTMLACM(self):
        pass
    
    def getEntryType(self):
        pass
    
    def getFormattedField(self, field):
        chars = dict()
        chars["{\\ss}"] = 'ss'
        chars["\\o"] = 'o'
        for i in range(ord('A'), ord('Z')) + range(ord('a'), ord('z')):
            chars["{\\c%s}" % chr(i)] = '%s' % chr(i)
            chars["\\r{%s}" % chr(i)] = '%s' % chr(i)
            chars["{\\'%s}" % chr(i)] = '%s' % chr(i)
            chars["{\\`%s}" % chr(i)] = '%s' % chr(i)
            chars["{\\\"%s}" % chr(i)] = '%s' % chr(i)
            chars["{\\^%s}" % chr(i)] = '%s' % chr(i)
            chars["\\~{%s}" % chr(i)] = '%s' % chr(i)
        value = self.getField(field)
        for i in chars.iterkeys():
            value.replace(i, chars[i])
        return value.replace('{', '').replace('}', '')
    
    def getHTMLFormattedField(self, field):
        chars = dict()
        chars["{\\ss}"] = '&szlig;'
        chars["\\o"] = '&oslash;'
        for i in range(ord('A'), ord('Z')) + range(ord('a'), ord('z')):
            chars["{\\c%s}" % chr(i)] = '&%scedil;' % chr(i)
            chars["\\r{%s}" % chr(i)] = '&%sring;' % chr(i)
            chars["{\\'%s}" % chr(i)] = '&%sacute;' % chr(i)
            chars["{\\`%s}" % chr(i)] = '&%sgrave;' % chr(i)
            chars["{\\\"%s}" % chr(i)] = '&%suml;' % chr(i)
            chars["{\\^%s}" % chr(i)] = '&%scirc;' % chr(i)
            chars["\\~{%s}" % chr(i)] = '&%stilde;' % chr(i)
        value = self.getField(field)
        for i in chars.iterkeys():
            value.replace(i, chars[i])
        return value.replace('{', '').replace('}', '').replace('\\url', '')