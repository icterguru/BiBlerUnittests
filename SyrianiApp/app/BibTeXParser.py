
from FieldName import FieldName
from EmptyEntry import EmptyEntry
from Article import Article
from Book import Book
from InProceedings import InProceedings
from PhDThesis import PhDThesis
from TechReport import TechReport
import re

class BibTeXParser(object):
    def __init__(self, bibtex):
        self.bibtex = bibtex
        self.re_header = re.compile("""\s*@(\w+)\s*[({]\s*(\w*)\s*""")
        self.re_field = re.compile("""\s*(\w+)\s*=\s*(.*)\s*,?""")
        
    def parse(self):
        # Get the type of entry first
        entry = None
        t = self.__findType()
        if t.lower() == 'article':
            entry = Article()
        elif t.lower() == 'book':
            entry = Book()
        elif t.lower() == 'inproceedings':
            entry = InProceedings()
        elif t.lower() == 'phdthesis':
            entry = PhDThesis()
        elif t.lower() == 'techreport':
            entry = TechReport()
        else:
            return EmptyEntry()
        # Set all required and optional fields
        for field in entry.requiredFields.keys():
            value = self.findField(field)
            entry.setField(field, value)
        for field in entry.optionalFields.keys():
            value = self.findField(field)
            entry.setField(field, value)
        return entry
        
    def findField(self, field):
        # Key is treated separately
        if field == FieldName.Key:
            return self.__findKey()
        
        # For all other fields
        lines = self.bibtex.splitlines()
        if len(lines) < 2:
            raise Exception('Invalid BibTeX.')
        del lines[0]
        for line in lines:
            result = self.re_field.match(line)
            if result is None:
                return ''
            elif result.group(1).lower() == field:
                value = result.group(2)
                if value.startswith('{{'):
                    return '{' + value.strip("""}"{,""")
                else:
                    return value.strip("""}"{,""")
        return ''
        
    def __findKey(self):
        lines = self.bibtex.splitlines()
        if len(lines) < 2:
            raise Exception('Invalid BibTeX.')
        header = self.re_header.match(lines[0])
        return header.group(2)
        
    def __findType(self):
        lines = self.bibtex.splitlines()
        if len(lines) < 2:
            raise Exception('Invalid BibTeX.')
        header = self.re_header.match(lines[0])
        return header.group(1)