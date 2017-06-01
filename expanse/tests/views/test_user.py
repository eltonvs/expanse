import unittest
from pyramid import testing

from expanse.views.user import UserViews


class UserViewTests(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()

        self.request = testing.DummyRequest()
        self.inst = UserViews(self.request)

    def tearDown(self):
        testing.tearDown()

    def test_register_user(self):
        res = self.inst.register_user()
        self.assertEqual('Sign up', res['page_title'])
