import unittest
from pyramid import testing


class ViewTests(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_index(self):
        from ..views.views import ExpanseViews

        request = testing.DummyRequest()
        inst = ExpanseViews(request)
        res = inst.index()
        self.assertEqual('Home', res['page_title'])
