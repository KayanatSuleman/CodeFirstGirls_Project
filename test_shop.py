import unittest
from shop import items_dict

class TestShop(unittest.TestCase):
    
    def test_items_dict_has_at_least_three_items(self):
        self.assertGreaterEqual(len(items_dict), 3)

if __name__ == '__main__':
    unittest.main()