# shopping_cart_example.py
from shopping_cart import ShoppingCart

def main():
    # Create an instance of ShoppingCart
    cart = ShoppingCart()

    # Add items to the cart
    cart.add_item('apple', 0.99)
    cart.add_item('banana', 0.59)
    cart.add_item('orange', 1.29)

    # Remove an item from the cart
    cart.remove_item('banana')

    # Get total item count
    total_items = cart.get_total_item_count()
    print(f'Total items: {total_items}')  # Output: Total items: 2

    # Get total price
    total_price = cart.get_total_price()
    print(f'Total price: ${total_price}')  # Output: Total price: $2.28

    # Get details of a single item
    apple_details = cart.get_item('apple')
    print(f'Apple details: {apple_details}')  # Output: Apple details: {'price': 0.99, 'quantity': 1}

    # Get details of a single item
    orange_details = cart.get_item('orange')
    print(f'Orange details: {orange_details}')

if __name__ == '__main__':
    main()
