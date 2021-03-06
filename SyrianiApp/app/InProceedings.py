
import Entry
from app.FieldName import FieldName

class InProceedings(Entry.Entry):
    def __init__(self):
        super(InProceedings, self).__init__()
        self.requiredFields = { FieldName.Author: '',
                                FieldName.Title: '',
                                FieldName.BookTitle: '',
                                FieldName.Year: ''}
        self.optionalFields = { FieldName.Editor: '',
                                FieldName.Volume: '',
                                FieldName.Number: '',
                                FieldName.Series: '',
                                FieldName.Pages: '',
                                FieldName.Organization: '',
                                FieldName.Publisher: '',
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
        booktitle = self.getHTMLFormattedField(FieldName.BookTitle)
        year = self.getHTMLFormattedField(FieldName.Year)
        editor = self.getHTMLFormattedField(FieldName.Editor)
        volume = self.getHTMLFormattedField(FieldName.Volume)
        number = self.getHTMLFormattedField(FieldName.Number)
        series = self.getHTMLFormattedField(FieldName.Series)
        pages = self.getHTMLFormattedField(FieldName.Pages)
        organization = self.getHTMLFormattedField(FieldName.Organization)
        publisher = self.getHTMLFormattedField(FieldName.Publisher)
        address = self.getHTMLFormattedField(FieldName.Address)
        month = self.getHTMLFormattedField(FieldName.Month)
        
        authors = getPeople(authors, 'author')
        
        html = '''<p><font face="verdana"><b><i>%s</i>(%s)</b></font></p>
<p><span style="font-variant:small-caps">%s</span> %s. In <i>%s</i>''' % (self.getEntryType(), self.optionalFields[FieldName.Key], authors, title, booktitle)
        if organization:
            html += ''', %s''' % organization
        html += ''' ('''
        if address:
            html += '''%s, ''' % address
        if month:
            html += '''%s ''' % month
        html += '''%s)''' % year
        if editor:
            html += ''', %s, Eds.''' %  getPeople(editor, 'editor')
        if volume:
            html += ''', vol. %s''' % volume
        if number:
            html += ''', %s''' % number
        if series:
            html += ''' of <i>%s</i>''' % series
        if publisher:
            html += ''', %s''' % publisher
        if pages:
            html += ''', pp. %s''' % pages
        html += '.</p>'
        
        return html
    
    def getEntryType(self):
        return 'INPROCEEDINGS'
        
    
