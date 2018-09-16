'''
Created on Jan 24, 2014

@author: mokter
'''
import unittest
from app.UserInterface  import  UserInterface
from gui.app_interface import EntryListColumn
from gui.app_interface import EntryDict


import random

class TestUserInterface(unittest.TestCase):

            
    def setUp(self):
        self.ui = UserInterface()
        self.seq = range(10)
        
        self.ui.LastId =10
        
        
        self.ui.Valid_entryId = 5
        self.ui.Invalid_entryId = -5
        
        self.ui.Valid_entryBibTeX1 ="@INPROCEEDINGS{Kiczales1997, author = {Kiczales, Gregor and Lamping, John and Mendhekar, Anurag and Maeda, Chris and Videira-Lopes, Cristina and Loingtier, Jean-Marc and Irwin, John}, title = {Aspect-Oriented Programming}, booktitle = {11th European Conference on Object-Oriented Programming}, year = {1997}, editor = {Askit, Mehmet and Matsuoka, Satoshi}, volume = {1241}, series = {Lecture Notes in Computer Science}, pages = {220-242}, address = {Jyvaskyla}, month = {jun}, publisher = {Springer-Verlag}}"
        self.ui.BibTeXRef = "@INPROCEEDINGS{Kiczales1997, author = {Kiczales, Gregor and Lamping, John and Mendhekar, Anurag and Maeda, Chris and Videira-Lopes, Cristina and Loingtier, Jean-Marc and Irwin, John}, title = {Aspect-Oriented Programming}, booktitle = {11th European Conference on Object-Oriented Programming}, year = {1997}, editor = {Askit, Mehmet and Matsuoka, Satoshi}, volume = {1241}, series = {Lecture Notes in Computer Science}, pages = {220-242}, address = {Jyvaskyla}, month = {jun}, publisher = {Springer-Verlag}}"
        
        self.ui.HTML_Rep_entry = "Kiczales, Gregor and Lamping, John and Mendhekar, Anurag and Maeda, Chris and Videira-Lopes, Cristina and Loingtier, Jean-Marc and Irwin, John, Aspect-Oriented Programming, 11th European Conference on Object-Oriented Programming, 1997, Askit, Mehmet and Matsuoka, Satoshi, 1241, Lecture Notes in Computer Science, 220-242, Jyvaskyla, jun, Springer-Verlag"
        
        
        self.ui.Invalid_entryBibTeX1 = "@ARTICLE{Hossain2014, author = {Hossain, Mokter and Gray, Jeff}}"
        self.ui.Invalid_entryBibTeX2 = ""
        
        self.ui.searchKeyAuthor = 'Kiczales, Gregor and Lamping, John and Mendhekar, Anurag and Maeda, Chris and Videira-Lopes, Cristina and Loingtier, Jean-Marc and Irwin, John'
        
        self.ui.SearchYear = "1997"
        
        self.ui.Valid_path =  "C:\BiBbler\bibliography.bib"
        self.ui.Invalid_path =  " " 
        
        self.ui.Valid_importFormat = ('.bib', '.csv', '.html')
        self.ui.Invalid_importFormat = ('.doc', '.txt', '.htm')
        
        self.ui.Valid_exportFormat = ('.bib', '.csv', '.html')
        self.ui.Invalid_exportFormat = ('.doc', '.txt', '.htm')
        
        
        self.ui.HasUndoableActionLeft = 0
        


    def tearDown(self):
        #pass
        self.ui.exit()
        self.ui = None
    
    
    def start(self): 
        self.ui = UserInterface()
        self.seq = range(10)
    
    def exit(self): 
        self.ui.exit()
        self.ui = None
    

     
              
    
    def testimportFile_Success(self):
        
        returnme = self.ui.importFile(self.ui.Valid_path, self.ui.Valid_importFormat) 
        self.assertTrue(returnme, msg= "Incorrect import for success ")

      
    def testimportFile_Both_Invalid(self):
        
        returnme = self.ui.importFile(self.ui.Invalid_path, self.ui.Invalid_importFormat) 
        self.assertFalse(returnme, msg= "Incorrect import for success ")
          
    def testimportFile_Fail_Invalid_importFormat(self):
        
        returnme = self.ui.importFile(self.ui.Valid_path, self.ui.Invalid_importFormat) 
        self.assertFalse(returnme, msg= "Incorrect import for success ")
          
    def testimportFile_Fail_Invalid_path(self):
        
        returnme = self.ui.importFile(self.ui.Invalid_path, self.ui.Valid_importFormat) 
        self.assertFalse(returnme, msg= "Incorrect import for success ")
    
    
    def testexportFile_Success(self):
        
        returnme = self.ui.exportFile(self.ui.Valid_path, self.ui.Valid_importFormat) 
        self.assertTrue(returnme, msg= "Incorrect import for success ")
              
    
    def testexportFile_Both_Invalid(self):
        
        returnme = self.ui.exportFile(self.ui.Invalid_path, self.ui.Invalid_exportFormat) 
        self.assertFalse(returnme, msg= "Incorrect import for success ")
    
    

    def testexportFile_Fail_Invalid_path(self):
        
        returnme = self.ui.importFile(self.ui.Invalid_path, self.ui.Valid_exportFormat) 
        self.assertFalse(returnme, msg= "Incorrect import for success ")
    

    def testexportFile_Fail_Invalid_exportFormat(self):
        
        returnme = self.ui.importFile(self.ui.Valid_path, self.ui.Invalid_exportFormat) 
        self.assertFalse(returnme, msg= "Incorrect import for success ")




        
    def testaddEntry_Valid_entryBibTeX(self):
        oldEntryCount = self.ui.getEntryCount()
        self.ui.addEntry("@INPROCEEDINGS{Kiczales1997, author = {Kiczales, Gregor and Lamping, John and Mendhekar, Anurag and Maeda, Chris and Videira-Lopes, Cristina and Loingtier, Jean-Marc and Irwin, John}, title = {Aspect-Oriented Programming}, booktitle = {11th European Conference on Object-Oriented Programming}, year = {1997}, editor = {Askit, Mehmet and Matsuoka, Satoshi}, volume = {1241}, series = {Lecture Notes in Computer Science}, pages = {220-242}, address = {Jyvaskyla}, month = {jun}, publisher = {Springer-Verlag}}")
               
        newEntryCount = self.ui.getEntryCount()
        self.assertEquals(newEntryCount, oldEntryCount + 1, msg = "Incorrect addEntry Count for valid entryBibTeX")
        
        
    def testaddEntry_Empty_entryBibTeX(self):
             
        oldEntryCount = self.ui.getEntryCount()
        self.ui.addEntry("")
        newEntryCount = self.ui.getEntryCount()
        self.assertEquals(newEntryCount, oldEntryCount + 1, msg = "Incorrect addEntry for None entryBibTeX")

    
    

    def testaddEntry_Failed_entryBibTeX(self):
             
        returnme = self.ui.addEntry("Failed")
                      
        self.assertIsNone(returnme, msg= "Incorrect addEntry for empty entryBibTeX")
        

    def testaddEntry_None_entryBibTeX(self):
             
        oldEntryCount = self.ui.getEntryCount()
        self.ui.addEntry("Mokter Hossain")
                      
        newEntryCount = self.ui.getEntryCount()
        self.assertEquals(newEntryCount, oldEntryCount + 1, msg = "Incorrect addEntry for None entryBibTeX")
    
    

    def testduplicateEntry_valid_entryId(self):
        oldcount = self.ui.getEntryCount()
        
        self.ui.duplicateEntry(self.ui.Valid_entryId)
        #self.ui.duplicateEntry(5)
        
        newcount = self.ui.getEntryCount()
        self.assertEquals(newcount, oldcount + 1, msg= "Incorrect duplicate for valid entryId")
        
        
    
    def testduplicateEntry_invalid_entryId(self):
        
        returnme = self.ui.duplicateEntry(-5)
                      
        self.assertIsNone(returnme, msg= "Incorrect duplicate for invalid entryBibTeX")
      


    def testupdateEntry_valid_both_input(self):
    
        returnme = self.ui.updateEntry (self.ui.Valid_entryId, self.ui.Valid_entryBibTeX1) 
        self.assertTrue(returnme, msg= "Incorrect update for valid entryId and valid entryBibTeX")


        
    def testupdateEntry_both_Invalid_input(self):
    
        returnme = self.ui.updateEntry (self.ui.Invalid_entryId, self.ui.Invalid_entryBibTeX1) 
        self.assertFalse(returnme, msg= "Incorrect update for invalid entryBibTeX")

        
    def testupdateEntry_Invalid_entryId(self):
    
        returnme = self.ui.updateEntry (self.ui.Invalid_entryId, self.ui.Valid_entryBibTeX1) 
        self.assertFalse(returnme, msg= "Incorrect update for invalid entryId")
        
        
    def testupdateEntry_Invalid_entryBibTeX(self):
    
        returnme = self.ui.updateEntry (self.ui.Valid_entryId, self.ui.Invalid_entryBibTeX1) 
        self.assertFalse(returnme, msg= "Incorrect update for invalid entryBibTeX")
      
         
    
    def testdeleteEntry_Valid_entryId(self):
                
        entryId= self.ui.addEntry("@INPROCEEDINGS{Kiczales1997, author = {Kiczales, Gregor and Lamping, John and Mendhekar, Anurag and Maeda, Chris and Videira-Lopes, Cristina and Loingtier, Jean-Marc and Irwin, John}, title = {Aspect-Oriented Programming}, booktitle = {11th European Conference on Object-Oriented Programming}, year = {1997}, editor = {Askit, Mehmet and Matsuoka, Satoshi}, volume = {1241}, series = {Lecture Notes in Computer Science}, pages = {220-242}, address = {Jyvaskyla}, month = {jun}, publisher = {Springer-Verlag}}")
        returnme = self.ui.deleteEntry(entryId)
        
        self.assertTrue(returnme, msg= "DeleteEntry failed for incorrect entryId")
        
             
    
    def testdeleteEntry_Invalid_entryId(self):
        returnme = self.ui.deleteEntry(-5)
        self.assertFalse(returnme, msg= "DeleteEntry failed for incorrect entryId")
        

        
    
    def testpreviewEntry(self):
        
        entryId= self.ui.addEntry("@INPROCEEDINGS{Kiczales1997, author = {Kiczales, Gregor and Lamping, John and Mendhekar, Anurag and Maeda, Chris and Videira-Lopes, Cristina and Loingtier, Jean-Marc and Irwin, John}, title = {Aspect-Oriented Programming}, booktitle = {11th European Conference on Object-Oriented Programming}, year = {1997}, editor = {Askit, Mehmet and Matsuoka, Satoshi}, volume = {1241}, series = {Lecture Notes in Computer Science}, pages = {220-242}, address = {Jyvaskyla}, month = {jun}, publisher = {Springer-Verlag}}")
        
        HTML_Rep= self.ui.previewEntry(entryId)
        
        self.assertEqual(self.ui.HTML_Rep_entry, HTML_Rep, msg="Invalid preview ")
         
        
            
           
                
    def testgetEntryPaperURL_Success(self):
 
        paperURL= self.ui.getEntryPaperURL("@INPROCEEDINGS{Kiczales1997, author = {Kiczales, Gregor and Lamping, John and Mendhekar, Anurag and Maeda, Chris and Videira-Lopes, Cristina and Loingtier, Jean-Marc and Irwin, John}, title = {Aspect-Oriented Programming}, booktitle = {11th European Conference on Object-Oriented Programming}, year = {1997}, editor = {Askit, Mehmet and Matsuoka, Satoshi}, volume = {1241}, series = {Lecture Notes in Computer Science}, pages = {220-242}, address = {Jyvaskyla}, month = {jun}, publisher = {Springer-Verlag}}")
        
        entryDict = self.ui.getEntry(paperURL)
        self.assertEquals(entryDict[EntryListColumn.PAPER], paperURL, msg="Invalid Paper URL")
        

    
    def testsearch_Success(self):
            
        dictItem = EntryDict()
        # ###. . . . . . . 
        returnme = self.ui.search("Success")
        self.assertTrue(returnme, msg= "Search failed for incorrect matched query")
        
        
    
    def testsearch_Fail(self):
        
        dictItem = EntryDict()
        ##. .. . . . . .       
        returnme = self.ui.search("Fail")
        self.assertFalse(returnme, msg= "DeleteEntry failed for incorrect entryId")
        
                    
    def testsearch_NoResult(self):
        
        dictItem = EntryDict()
        ##. .. . . . . .       
        returnme = self.ui.search("")
        self.assertTrue(returnme, msg= "Search failed for no result query")

    
    
    def testsort_Success(self):
            
        dictItem = EntryDict()
        # ###. . . . . . . 
        returnme = self.ui.sort("Sorted")
        self.assertTrue(returnme, msg= "Sort failed for incorrect sorted field")
        
        
    def testsort_Fail(self):
        
        dictItem = EntryDict()
        ##. .. . . . . .       
        returnme = self.ui.sort("Fail")
        self.assertFalse(returnme, msg= "Sort failed for incorrect unsorted field")
    
        
                    
    def testsort_Otherwise(self):
        
        dictItem = EntryDict()
        ##. .. . . . . .       
        returnme = self.ui.sort("Not Sorted")
        self.assertFalse(returnme, msg= "Sort failed for incorrect unsorted field")
    
        

    def testgetEntry_Success(self):
        
        entryId= self.ui.addEntry("@INPROCEEDINGS{Kiczales1997, author = {Kiczales, Gregor and Lamping, John and Mendhekar, Anurag and Maeda, Chris and Videira-Lopes, Cristina and Loingtier, Jean-Marc and Irwin, John}, title = {Aspect-Oriented Programming}, booktitle = {11th European Conference on Object-Oriented Programming}, year = {1997}, editor = {Askit, Mehmet and Matsuoka, Satoshi}, volume = {1241}, series = {Lecture Notes in Computer Science}, pages = {220-242}, address = {Jyvaskyla}, month = {jun}, publisher = {Springer-Verlag}}")
        entryDict = self.ui.getEntry(entryId)
             
        self.assertEquals(entryDict[EntryListColumn.ID], entryId, msg="Invalid entryId for ")
        
    
    
    def testgetEntry_Fail(self):
        
        entryId= self.ui.addEntry("@INPROCEEDINGS{Kiczales1997, author = {Kiczales, Gregor and Lamping, John and Mendhekar, Anurag and Maeda, Chris and Videira-Lopes, Cristina and Loingtier, Jean-Marc and Irwin, John}, title = {Aspect-Oriented Programming}, booktitle = {11th European Conference on Object-Oriented Programming}, year = {1997}, editor = {Askit, Mehmet and Matsuoka, Satoshi}, volume = {1241}, series = {Lecture Notes in Computer Science}, pages = {220-242}, address = {Jyvaskyla}, month = {jun}, publisher = {Springer-Verlag}}")
        entryDict = self.ui.getEntry(-5)
                     
        self.assertNotEqual(entryDict[EntryListColumn.ID], entryId, msg="Invalid entryId for ")
        
  
    def testgetBibTeX_Success(self):
        entryId= self.ui.addEntry("@INPROCEEDINGS{Kiczales1997, author = {Kiczales, Gregor and Lamping, John and Mendhekar, Anurag and Maeda, Chris and Videira-Lopes, Cristina and Loingtier, Jean-Marc and Irwin, John}, title = {Aspect-Oriented Programming}, booktitle = {11th European Conference on Object-Oriented Programming}, year = {1997}, editor = {Askit, Mehmet and Matsuoka, Satoshi}, volume = {1241}, series = {Lecture Notes in Computer Science}, pages = {220-242}, address = {Jyvaskyla}, month = {jun}, publisher = {Springer-Verlag}}")
                      
        BibTeX_Rep = self.ui.getBibTeX(entryId)
        
        self.assertNotEqual(self.ui.Valid_entryBibTeX1, BibTeX_Rep, msg="Invalid BibTeX ")   

   
        
    def testgetAllEntries_Success(self):
        allEntries = self.ui.getAllEntries()
        size_allListItems = len(allEntries)
        size_allDictItems =len(self.ui.EntryDict)
        self.assertEquals(size_allListItems, size_allDictItems, msg="Invalid conversion ")
                

    
    def testgetEntryCount(self):
        
        entryCount = self.ui.getEntryCount()
        
        entryListCount = len(self.ui.entryList)    
        self.assertEquals(entryCount, entryListCount, msg="Invalid Paper URL")
        #len(self.entryList)
                
    
        
    def testSearchResult_Success(self):
        allEntries = self.ui.getAllEntries()
        size_allListItems = len(allEntries)
        size_allDictItems =len(self.ui.EntryDict)
        self.assertEquals(size_allListItems, size_allDictItems, msg="Invalid conversion ")
                    

    def testAddDeleteSanity(self):
        
        beforeAddEntryCount = self.ui.getEntryCount()
        
        entryId = self.ui.addEntry("@INPROCEEDINGS{Kiczales1997, author = {Kiczales, Gregor and Lamping, John and Mendhekar, Anurag and Maeda, Chris and Videira-Lopes, Cristina and Loingtier, Jean-Marc and Irwin, John}, title = {Aspect-Oriented Programming}, booktitle = {11th European Conference on Object-Oriented Programming}, year = {1997}, editor = {Askit, Mehmet and Matsuoka, Satoshi}, volume = {1241}, series = {Lecture Notes in Computer Science}, pages = {220-242}, address = {Jyvaskyla}, month = {jun}, publisher = {Springer-Verlag}}")
                   
        afterAddEntryCount = self.ui.getEntryCount()
          
        #self.assertEqual(afterAddEntryCount, beforeAddEntryCount +1, msg = "Incorrect add/delete consistency")     
        
        self.ui.deleteEntry(entryId)
  
        afterDeleteEntryCount = self.ui.getEntryCount()
                       
        
        self.assertEqual(beforeAddEntryCount, afterDeleteEntryCount, msg = "Incorrect add/delete consistency")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
    