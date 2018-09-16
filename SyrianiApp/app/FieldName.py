from gui.app_interface import EntryListColumn

class FieldName:
    Address = 'address'
    Author = 'author'
    BookTitle = 'booktitle'
    Edition = 'edition'
    Editor = 'editor'
    Institution = 'institution'
    Journal = 'journal'
    Key = 'key'
    Month = 'month'
    Note = 'note'
    Number = 'number'
    Organization = 'organization'
    Pages = 'pages'
    Paper = 'paper'
    Publisher = 'publisher'
    School = 'school'
    Series = 'series'
    Title = 'title'
    Type = 'type'
    Volume = 'volume'
    Year = 'year'
    
    @staticmethod
    def toEntryListColumn(field):
        if field == FieldName.Author: return EntryListColumn.AUTHOR
        elif field == FieldName.Key: return EntryListColumn.KEY
        elif field == FieldName.Paper: return EntryListColumn.PAPER
        elif field == FieldName.Title: return EntryListColumn.TITLE
        elif field == FieldName.Year: return EntryListColumn.YEAR
        else:
            return field
    
    @staticmethod
    def fromEntryListColumn(column):
        if column == EntryListColumn.AUTHOR: return FieldName.Author
        elif column == EntryListColumn.KEY: return FieldName.Key
        elif column == EntryListColumn.PAPER: return FieldName.Paper
        elif column == EntryListColumn.TITLE: return FieldName.Title
        elif column == EntryListColumn.YEAR: return FieldName.Year
        else:
            raise Exception('The column is not an EntryColumnList.')
    
    @staticmethod
    def getAllFields():
        return [FieldName.Address, FieldName.Author, FieldName.BookTitle, FieldName.Edition, FieldName.Editor,
                FieldName.Institution, FieldName.Journal, FieldName.Key, FieldName.Month, FieldName.Note, FieldName.Number,
                FieldName.Organization, FieldName.Pages, FieldName.Paper, FieldName.Publisher, FieldName.School,
                FieldName.Series, FieldName.Title, FieldName.Type, FieldName.Volume, FieldName.Year]