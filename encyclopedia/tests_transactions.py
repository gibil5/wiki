"""
Test HTTP Transactions
    Created:    28 dec 2020
    Last up:     7 Jan 2021
"""
import unittest
from django.test import Client
from . import util
from . import lib as x

SKIP_REQ_TESTS = 0

# ------------------------------------------------------------------------------
#                              Test Transactions
# ------------------------------------------------------------------------------
#@unittest.skip
@unittest.skipIf(SKIP_REQ_TESTS, 'x')
class SimpleTest(unittest.TestCase):
    """
    Transaction tests
    Tests entry requests
    """
    def setUp(self):
        """
        Setup
        """
        self.prefix = '\n\n'
        self.client = Client()
        self.pages = ['css', 'html', 'git', 'django', 'python']
        self.pages_ne = ['non_existant']
        self.verbose = True
        #self.verbose = False

    #@unittest.skip
    def test_index(self):
        """
        Index entries
        GET request
        """
        x.printx(f"{self.prefix}test_index")
        response = self.client.get('/')
        #if self.verbose:
        #    util.print_response(response)

    #@unittest.skip
    def test_show(self):
        """
        Show entry
        GET request
        """
        x.printx(f"{self.prefix}test_show")

        fnames = ['Css', 'HTML', 'Git', 'Django', 'Python', 'ne']
        pages = ['CSS', 'HTML', 'Git', 'Django', 'Python', 'ne']
        #pages = ['CSS', 'HTML', 'Git', 'Django', 'Python']
        #pages = ['ne']

        error_msg = 'Error: The requested page was not found.'
        #x.printx(util.list_entries())

        #for page in pages:
        for fname, page in zip(fnames, pages):
            request = f"/wiki/{page}/"

            response = self.client.get(request)

            # Check that the response is 200 OK.
            self.assertEqual(response.status_code, 200)

            # Check that the page has the correct title.
            title = util.parse_title(str(response.content))
            x.printx(f'\n{title}, {page}')

            # If the page exists
            if fname in util.list_entries():
                self.assertEqual(title, page)
            # If the page does not exist
            else:
                self.assertEqual(title, error_msg)


    #@unittest.skip
    def test_search(self):
        """
        Search entry
        GET request
        """
        x.printx(f"{self.prefix}test_search")

        #fnames = ['Css']
        #pages = ['CSS']
        fnames = ['Css', 'HTML', 'Git', 'Django', 'Python', 'py', 'x']
        pages = ['CSS', 'HTML', 'Git', 'Django', 'Python', 'py', 'x']

        warning_msg = 'It might be here.'
        error_msg = 'Error: The requested page was not found.'

        #for page in pages:
        for fname, page in zip(fnames, pages):
            request = f"/search/?q={page}"
            response = self.client.get(request)

            # Check that the response is 200 OK
            self.assertEqual(response.status_code, 200)

            # Check that the page has the correct title
            title = util.parse_title(str(response.content))
            x.printx(f'\n{title}, {page}')

            # If the page exists
            if fname in util.list_entries():
                self.assertEqual(title, page)
            # If the term is a substring
            #elif (entries := util.is_subtring(page, util.list_entries())):
            elif (entries := util.is_subtring(page, util.list_entries())) != None:
                self.assertEqual(title, warning_msg)
            # The term is not a substring
            else:
                self.assertEqual(title, error_msg)


    #@unittest.skip
    def test_create_get(self):
        """
        Create entry
        GET
        """
        x.printx(f"{self.prefix}test_create_get")

        request = "/create/"
        response = self.client.get(request)

        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check that the page has the correct title
        title = util.parse_title(str(response.content))
        #x.printx(f'\n{title}')

        # The page exists
        self.assertEqual(title, 'Create')

        # Check inputs
        input_title = util.parse_inputs(str(response.content), 'input', 'title')
        x.printx(f'{input_title}')
        input_content = util.parse_inputs(str(response.content), 'textarea', 'content')
        x.printx(f'{input_content}')
        input_submit = util.parse_inputs(str(response.content), 'input', 'submit')
        x.printx(f'{input_submit}')


    @unittest.skip
    def test_create_post(self):
        """
        Create entry
        POST

        (fv, tv)[test()]

        (x.printx(msg), pass)[verb()]
        (x.printx(msg), )[verb()]

        x.printx(msg) if verb() else pass
        printx(msg)
        """
        x.printx(f"{self.prefix}test_create_post")

        # Init
        title = 'Test'
        content = 'This is the content...'
        util.delete_entry(title)

        # Entry is created - success
        msg = '\n\nEntry is created'
        x.printx(msg)
        response = self.client.post('/create/', {'title': {title}, 'content': {content}})
        x.printx(response)

        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check page
        title = util.parse_title(str(response.content))
        x.printx(f'Title: {title}')
        self.assertEqual(title, 'Test')


        # Entry is not created: already exists - error
        msg = '\n\nEntry is not created: already exists'
        x.printx(msg)
        response = self.client.post('/create/', {'title': {title}, 'content': {content}})
        x.printx(response)
        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)
        # Check page
        title = util.parse_title(str(response.content))
        x.printx(f'Title: {title}')
        self.assertEqual(title, 'Error: Entry already exists !')

        # Form is not valid - error
        msg = '\n\nForm is not valid'
        x.printx(msg)
        response = self.client.post('/create/', {'title_x': {title}, 'content': {content}})
        x.printx(response)
        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)
        # Check page
        title = util.parse_title(str(response.content))
        x.printx(f'Title: {title}')
        self.assertEqual(title, 'Error: Form is not valid !')
