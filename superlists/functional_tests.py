from selenium import webdriver
import unittest

class NewVistiorTest(unittest.TestCase):
    def setUp(self):       
        self.browser = webdriver.Firefox(executable_path = 'F:\Mozilla Firefox\geckodriver.exe')

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):    
        self.browser.get('http://localhost:8000')

        #assert 'Django' in browser.title
        self.assertIn('To-Do',self.browser.title)
        self.fail('Finissh the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
