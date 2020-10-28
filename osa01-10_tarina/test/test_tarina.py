import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.tarina'

@points('1.tarina')
class TarinaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = ''):
            cls.module = load_module(exercise, 'fi')

    def test_tulostus_1(self):
        pieces = "Jarmo,1340"
        plist = pieces.split(",")
        with patch('builtins.input', side_effect = plist):
            reload_module(self.module)
            output = get_stdout().strip()
                     
            for piece in plist:
                self.assertTrue(output.find(piece) > -1, "Tulostuksesta ei löytynyt ollenkaan syötettä " + piece)
            
            story = plist[0] + " on urhea ritari, syntynyt vuonna " + plist[1] + "." 
            story += " Eräänä aamuna " + plist[0] + " heräsi kovaan meluun: lohikäärme lähestyi kylää. "
            story += "Vain " + plist[0] + " voisi pelastaa kylän asukkaat."
            output = output.replace("\n"," ")
            self.assertEqual(output.replace(" ", ""), story.replace(" ",""), "Tulostus ei ole esimerkin mukainen. Tulostus:\n {}, esimerkki:\n {}".format(output, story))

    def test_tulostus_2(self):
        pieces = "Kaarle Hirmuinen,1119"
        plist = pieces.split(",")
        with patch('builtins.input', side_effect = plist):
            reload_module(self.module)
            output = get_stdout().strip()
                     
            for piece in plist:
                self.assertTrue(output.find(piece) > -1, "Tulostuksesta ei löytynyt ollenkaan syötettä " + piece)
            
            story = plist[0] + " on urhea ritari, syntynyt vuonna " + plist[1] + "." 
            story += " Eräänä aamuna " + plist[0] + " heräsi kovaan meluun: lohikäärme lähestyi kylää. "
            story += "Vain " + plist[0] + " voisi pelastaa kylän asukkaat."
            output = output.replace("\n"," ")
            self.assertEqual(output.replace(" ", ""), story.replace(" ",""), "Tulostus ei ole esimerkin mukainen. Tulostus:\n {}, esimerkki:\n {}".format(output, story))

    def test_tulostus_3(self):
        pieces = "Arthur,1290"
        plist = pieces.split(",")
        with patch('builtins.input', side_effect = plist):
            reload_module(self.module)
            output = get_stdout().strip()
                     
            for piece in plist:
                self.assertTrue(output.find(piece) > -1, "Tulostuksesta ei löytynyt ollenkaan syötettä " + piece)
            
            story = plist[0] + " on urhea ritari, syntynyt vuonna " + plist[1] + "." 
            story += " Eräänä aamuna " + plist[0] + " heräsi kovaan meluun: lohikäärme lähestyi kylää. "
            story += "Vain " + plist[0] + " voisi pelastaa kylän asukkaat."
            output = output.replace("\n"," ")
            self.assertEqual(output.replace(" ", ""), story.replace(" ",""), "Tulostus ei ole esimerkin mukainen. Tulostus:\n {}, esimerkki:\n {}".format(output, story))

    
    
            
   
   
if __name__ == '__main__':
    unittest.main()
