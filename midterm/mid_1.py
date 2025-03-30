from typing import Self


class ShoppingCart:
    def __init__(self):
        self.__items = {}

    def add_item(self, name: str, price: float, quantity: int = 1) -> Self:
        """
        self.__items = {
            "Apple": {
                0.5: 2,
                0.1: 3,
                ...
            },
            ...
        }
        :raises ValueError: for non-valid arguments. E.g. price <= 0; quantity <= 0.
        """
        ...
        return self

    def __len__(self) -> int:
        ...

    def __str__(self) -> str:
        ...


if __name__ == '__main__':
    cart = ShoppingCart()
    cart.add_item('Apple', 0.5, 3)
    cart.add_item('Banana', 0.3, 5)
    cart.add_item('Apple', 0.5, 2)
    cart.add_item('Apple', 0.1, 3)
    # You may implement fluent interface as well:
    # cart.add_item('Apple', 0.5, 3).add_item('Banana', 0.3, 5).add_item('Apple', 0.5, 2)
    print(cart)  # Should display the items and total cost
    print(f"Total items: {len(cart)}")  # Should display total unique items in the cart

    """
    For validation unittests
    with self.assertRaises(ValueError):
        cart.add_item('Banana', 0.1, -2)
    """
