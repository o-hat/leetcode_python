import unittest


class TestKey(unittest.TestCase):

    def test_key(self):
        a = "asd"
        b = "asda"
        self.assertEqual(a, b)
        assert a == b