import unittest
from hello import hello as h

class TestHello(unittest.TestCase):
    def test_equal(self):
        self.assertEqual('Hello', h())

if __name__ == '__main__':
    unittest.main()