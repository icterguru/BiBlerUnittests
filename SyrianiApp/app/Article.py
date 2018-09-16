
import Entry
from app.FieldName import FieldName

class Article(Entry.Entry):
    def __init__(self):
        super(Article, self).__init__()
        self.requiredFields = { FieldName.Author: '',
                                FieldName.Title: '',
                                FieldName.Journal: '',
                                FieldName.Year: ''}
        self.optionalFields = { FieldName.Volume: '',
                                FieldName.Number: '',
                                FieldName.Pages: '',
                                FieldName.Month: '',
                                FieldName.Note: '',
                                FieldName.Key: '',
                                FieldName.Paper: ''}
        
    def toHTMLIEEETrans(self):
        pass
        
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
        journal = self.getHTMLFormattedField(FieldName.Journal)
        year = self.getHTMLFormattedField(FieldName.Year)
        volume = self.getHTMLFormattedField(FieldName.Volume)
        number = self.getHTMLFormattedField(FieldName.Number)
        pages = self.getHTMLFormattedField(FieldName.Pages)
        month = self.getHTMLFormattedField(FieldName.Month)
        
        authors = getPeople(authors, 'author')
        
        html = '''<p><font face="verdana"><b><i>%s</i>(%s)</b></font></p>
<p><span style="font-variant:small-caps">%s</span> %s <i>%s</i>''' % (self.getEntryType(), self.optionalFields[FieldName.Key], authors, title, journal)
        if volume:
            html += ''' <i>%s</i>''' % volume
        if number:
            html += ''', %s''' % number
        html += ''' ('''
        if month:
            html += '''%s ''' % month
        html += '''%s)''' % year
        if pages:
            html += ''', %s''' % pages
        html += '.</p>'
        
        return html
    
    def getEntryType(self):
        return 'ARTICLE'
        
    
