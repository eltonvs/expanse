import unittest
from pyramid import testing

from expanse.views.views import ExpanseViews


class ExpanseViewTests(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()

        self.request = testing.DummyRequest()
        self.inst = ExpanseViews(self.request)

    def tearDown(self):
        testing.tearDown()

    def test_index(self):
        res = self.inst.index()
        self.assertEqual('Home', res['page_title'])

    def test_login(self):
        res = self.inst.login()
        self.assertEqual('Login', res['page_title'])
