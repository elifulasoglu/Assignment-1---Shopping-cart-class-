class ShoppingCart:
    """Class to represent a shopping cart."""

    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = {}

    def add_item(self, item_name, price):
        """
        Add an item to the shopping cart.

        Args:
            item_name (str): The name of the item to add.
            price (float): The price of the item.
        """
        if item_name in self.items:
            self.items[item_name]['quantity'] += 1
        else:
            self.items[item_name] = {'price': round(price, 2), 'quantity': 1}

    def remove_item(self, item_name):
        """
        Remove an item from the shopping cart.

        Args:
            item_name (str): The name of the item to remove.
        """
        if item_name in self.items:
            if self.items[item_name]['quantity'] > 1:
                self.items[item_name]['quantity'] -= 1
            else:
                del self.items[item_name]

    def get_total_item_count(self):
        """
        Get the total number of items in the shopping cart.

        Returns:
            int: Total number of items.
        """
        return sum(item['quantity'] for item in self.items.values())

    def get_total_price(self):
        """
        Get the total price of all items in the shopping cart.

        Returns:
            float: Total price of all items.
        """
        return round(sum(item['price'] * item['quantity'] for item in self.items.values()), 2)

    def get_item(self, item_name):
        """
        Get the details of a single item in the shopping cart.

        Args:
            item_name (str): The name of the item to get details for.

        Returns:
            dict or None: The details of the item, or None if the item is not in the cart.
        """
        return self.items.get(item_name)
