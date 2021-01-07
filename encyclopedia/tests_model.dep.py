"""
Test suite
    Created:    28 dec 2020
    Last up:     3 Jan 2021
"""
import unittest
import inspect
from django.test import Client

# Create your tests here.
#SKIP_LIB_TESTS = 0
#SKIP_REQ_TESTS = 0
SKIP_MODEL_TESTS = 1

# ------------------------------------------------------------------------------
#                              Test Model Page
# ------------------------------------------------------------------------------
#@unittest.skip
@unittest.skipIf(SKIP_MODEL_TESTS, 'x')
class ModelPageTestCase(unittest.TestCase):
    """
    Unit tests
    For the model Page
    """
    def __init__(self, *args, **kwargs):
        super(ModelPageTestCase, self).__init__(*args, **kwargs)

    def setUp(self):
        """
        Setup
        """
        self.prefix = '\n\n'


    #@unittest.skip
    def test_model_migrate_pages(self):
        """
        Create pages, from existing entries
        """
        print(f"{self.prefix}test_model_migrate_pages")
        #this_function_name = inspect.currentframe().f_code.co_name
        #print(f"{self.prefix}{this_function_name}")
        #titles = ['Python']
        #titles = ['HTML']
        titles = util.list_entries()
        for title in titles:
            entry = util.get_entry(title)
            first_line = entry.split('\n', 1)[0]
            rest = entry.split('\n', 1)[1]
            #print(first_line)
            #print(rest)
            name = title.lower()
            page = util.create_page(name, first_line, rest)
            #print(page)
            #self.assertEqual(list_entries, self.list)


    #@unittest.skip
    def test_model_delete_pages(self):
        """
        Delete pages
        """
        print(f"{self.prefix}test_model_delete_pages")
        names = ['page_1', 'page_2', 'page_3']
        #from name in names:
        for name in zip(names):
            #print(f'{name[0]}')
            page = util.delete_page(name[0])
            #print(page)
            #self.assertEqual(list_entries, self.list)

    #@unittest.skip
    def test_model_create_pages(self):
        """
        Create pages
        """
        print(f"{self.prefix}test_model_create_pages")
        names = ['page_1', 'page_2', 'page_3']
        titles = ['Page 1', 'Page 2', 'Page 3']
        contents = [ 'This is the content for **page1**...',
                    'This is the content for **page2**...',
                    'This is the content for **page3**...',
                ]

        #from name in names:
        for name, title, content in zip(names, titles, contents):
            #print(f'{name}, {title}, {content}')
            page = util.create_page(name, title, content)
            #print(page)
            #self.assertEqual(list_entries, self.list)

