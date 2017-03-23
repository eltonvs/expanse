import unittest

from pyramid import testing

class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from expanse import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_root(self):
        res = self.testapp.get('/', status=200)
        self.assertTrue(b'expanse' in res.body)
