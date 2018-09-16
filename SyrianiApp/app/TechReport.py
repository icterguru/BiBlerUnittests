
import Entry
from app.FieldName import FieldName

class TechReport(Entry.Entry):
    def __init__(self):
        super(TechReport, self).__init__()
        self.requiredFields = { FieldName.Author: '',
                                FieldName.Title: '',
                                FieldName.Institution: '',
                                FieldName.Year: ''}
        self.optionalFields = { FieldName.Type: '',
                                FieldName.Number: '',
                                FieldName.Address: '',
                                FieldName.Month: '',
                                FieldName.Note: '',
                                FieldName.Key: '',
                                FieldName.Paper: ''}
        
    def toHTMLIEEETrans(self):
        return ''
        
    def toHTMLACM(self):
        def getPeople(people, fieldName):
            try:
                a = people.split(' and ')
                for i in xrange(len(a)):
                    a[i] = a[i].split(',')
                    if len(a[i]) == 2:
                        a[i] = '%s, %s.' % (a[i][0], a[i][1].strip().upper()[0])
                if len(a) == 1:
                    people = ', '.join(a)
                else:
                    people = ', '.join(a[:-1])
                    people = '%s, and %s' % (people, a[-1])
                if people[-1] != '.':
                    people += '.'
                return people
            except:
                raise Exception('Invalid %s names.' % fieldName)
        
        # Capital letters are already between {}
        authors = self.getHTMLFormattedField(FieldName.Author)
        title = self.getHTMLFormattedField(FieldName.Title)
        institution = self.getHTMLFormattedField(FieldName.Institution)
        year = self.getHTMLFormattedField(FieldName.Year)
        _type = self.getHTMLFormattedField(FieldName.Type)
        number = self.getHTMLFormattedField(FieldName.Number)
        address = self.getHTMLFormattedField(FieldName.Address)
        month = self.getHTMLFormattedField(FieldName.Month)
        
        authors = getPeople(authors, 'author')
        
        html = '''<p><font face="verdana"><b><i>%s</i>(%s)</b></font></p>
<p><span style="font-variant:small-caps">%s</span> %s. ''' % (self.getEntryType(), self.optionalFields[FieldName.Key], authors, title)
        if _type:
            html += '''%s, ''' % _type
        if number:
            html += '''%s, ''' % number
        html += '''%s, ''' % institution
        if address:
            html += '''%s, ''' % address
        if month:
            html += '''%s ''' % month
        html += '''%s''' % year
        html += '.</p>'
        
        return html
    
    def getEntryType(self):
        return 'TECHREPORT'
        
    
