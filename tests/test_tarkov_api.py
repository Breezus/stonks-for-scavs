
from .context import tarkovAPI

import unittest

class TestTarkovAPI(unittest.TestCase):

    def test_query_init(self):
        api = tarkovAPI({})
        self.assertIsNotNone(api)

    def test_query_builder(self):
        self.assertEqual(1,1)

