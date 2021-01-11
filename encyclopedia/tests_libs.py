"""
Test Libs - Util

    Created:    28 dec 2020
    Last up:     7 jan 2021
"""
import unittest
import inspect
from django.test import Client
from . import util
from . import lib as x

SKIP_LIB_TESTS = 0

# ------------------------------------------------------------------------------
#                              Test Util library
# ------------------------------------------------------------------------------
#@unittest.skip
@unittest.skipIf(SKIP_LIB_TESTS, 'x')
class UtilLibraryTestCase(unittest.TestCase):
    """
    Unit tests
    For the Util library
    """
    def setUp(self):
        """
        Setup
        """
        self.prefix = '\n\n'
        self.list = ['Css', 'Django', 'Git', 'HTML', 'Python', 'Test']
        self.entry = "# Python\n\nPython is a programming language that can be used both for writing **command-line scripts** or building **web applications**."


    #@unittest.skip
    def test_lib_list_entries(self):
        """
        List of entries
        """
        print(f"{self.prefix}test_lib_list_entries")
        list_entries = util.list_entries()
        self.assertEqual(list_entries, self.list)


    #@unittest.skip
    def test_lib_get_entry(self):
        """
        Get entry
        """
        print(f"{self.prefix}test_lib_get_entry")
        titles = ['python', 'not_available']

        for title in titles:
            try:
                entry = util.get_entry(title=title)
            except FileNotFoundError:
                x.printx('\nERROR')
                x.printx('File not found !')
            else:
                x.printx('\nSUCCESS')
                self.assertEqual(entry, self.entry)



    #@unittest.skip
    def test_lib_create_del_entry(self):
        """
        Save entry
        Deletes entry
        """
        print(f"{self.prefix}test_lib_create_del_entry")
        titles = ['Test 1', 'Test 2', 'Test 3']
        content = 'This is the **test** content...'
        for title in titles:
            util.save_entry(title=title, content=content)
            #self.assertEqual(list_entries, self.list)
        for title in titles:
            util.delete_entry(title=title)
            #self.assertEqual(list_entries, self.list)


    #@unittest.skip
    def test_lib_sub_success(self):
        """
        Is substring success
        """
        print(f"{self.prefix}test_lib_sub_success")
        query = 'PY'
        titles = util.is_subtring(query=query, x_list=self.list)
        self.assertEqual(titles, ['python'])


    #@unittest.skip
    def test_lib_sub_failure(self):
        """
        Is substring failure
        """
        print(f"{self.prefix}test_lib_sub_failure")
        query = 'x'
        titles = util.is_subtring(query=query, x_list=self.list)
        self.assertEqual(titles, None)
