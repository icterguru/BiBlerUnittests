
import Entry
from app.FieldName import FieldName

class Book(Entry.Entry):
    def __init__(self):
        super(Book, self).__init__()
        self.requiredFields = { FieldName.Author: '',
                                FieldName.Editor: '',
                                FieldName.Title: '',
                                FieldName.Publisher: '',
                                FieldName.Year: ''}
        self.optionalFields = { FieldName.Volume: '',
                                FieldName.Number: '',
                                FieldName.Series: '',
                                FieldName.Address: '',
                                FieldName.Edition: '',
                                FieldName.Month: '',
                                FieldName.Note: '',
                                FieldName.Key: '',
                                FieldName.Paper: ''}
        
    def validate(self):
        author_editor_check = (self.requiredFields[FieldName.Author] and not self.requiredFields[FieldName.Editor]) \
                        or (self.requiredFields[FieldName.Editor] and not self.requiredFields[FieldName.Author])
        return self.requiredFields[FieldName.Title] and self.requiredFields[FieldName.Publisher] \
                and self.requiredFields[FieldName.Year] and author_editor_check
        
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
        editor = self.getHTMLFormattedField(FieldName.Editor)
        title = self.getHTMLFormattedField(FieldName.Title)
        publisher = self.getHTMLFormattedField(FieldName.Publisher)
        year = self.getHTMLFormattedField(FieldName.Year)
        volume = self.getHTMLFormattedField(FieldName.Volume)
        number = self.getHTMLFormattedField(FieldName.Number)
        series = self.getHTMLFormattedField(FieldName.Series)
        address = self.getHTMLFormattedField(FieldName.Address)
        edition = self.getHTMLFormattedField(FieldName.Edition)
        month = self.getHTMLFormattedField(FieldName.Month)
        
        html = '''<p><font face="verdana"><b><i>%s</i>(%s)</b></font></p>
''' % (self.getEntryType(), self.optionalFields[FieldName.Key])
        if authors:
            html += '''<p><span style="font-variant:small-caps">%s</span>''' % getPeople(authors, 'author')
        else:
            html += '''<p><span style="font-variant:small-caps">%s</span>''' % getPeople(editor, 'editor')
        html += ''' <i>%s</i>''' % title
        if edition:
            html += ''', %s ed.''' % edition
        if volume:
            html += ''', vol. %s''' % volume
        if number:
            html += ''', %s''' % number
        if series:
            html += ''' of <i>%s</i>''' % series
        html += '''. %s, ''' % publisher
        if address:
            html += '''%s, ''' % address
        if month:
            html += '''%s''' % month
        html += ''' %s''' % year
        html += '.</p>'
        
        return html
    
    def getEntryType(self):
        return 'BOOK'
        
    
