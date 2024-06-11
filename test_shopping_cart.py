import unittest
from shopping_cart import ShoppingCart


class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        """Set up the test case environment."""
        self.cart = ShoppingCart()
        self.cart.add_item('apple', 0.99)
        self.cart.add_item('banana', 0.59)

    def test_add_item(self):
        """Test adding items to the cart."""
        self.cart.add_item('orange', 1.29)
        self.assertEqual(self.cart.get_item('orange'), {'price': 1.29, 'quantity': 1})

    def test_remove_item(self):
        """Test removing items from the cart."""
        self.cart.add_item('banana', 0.59)
        self.cart.remove_item('banana')
        self.assertEqual(self.cart.get_item('banana'), {'price': 0.59, 'quantity': 1})
        self.cart.remove_item('banana')
        self.assertIsNone(self.cart.get_item('banana'))

    def test_get_total_item_count(self):
        """Test getting the total item count."""
        self.assertEqual(self.cart.get_total_item_count(), 2)
        self.cart.add_item('apple', 0.99)
        self.assertEqual(self.cart.get_total_item_count(), 3)

    def test_get_total_price(self):
        """Test getting the total price of all items."""
        self.assertEqual(self.cart.get_total_price(), 1.58)
        self.cart.add_item('apple', 0.99)
        self.assertEqual(self.cart.get_total_price(), 2.57)

    def test_get_item(self):
        """Test getting a single item."""
        self.assertEqual(self.cart.get_item('apple'), {'price': 0.99, 'quantity': 1})
        self.assertIsNone(self.cart.get_item('orange'))


if __name__ == '__main__':
    unittest.main()
