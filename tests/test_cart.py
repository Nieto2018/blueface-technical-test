from shoppingcart.cart import ShoppingCart

import unittest


class TestCartMethods(unittest.TestCase):

    def test_add_item(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1)

        receipt = cart.print_receipt()

        assert receipt[0] == "apple - 1 - €1.00"

    def test_add_item_with_multiple_quantity(self):
        cart = ShoppingCart()
        cart.add_item("apple", 2)

        receipt = cart.print_receipt()

        assert receipt[0] == "apple - 2 - €2.00"

    def test_add_different_items(self):
        cart = ShoppingCart()
        cart.add_item("banana", 1)
        cart.add_item("kiwi", 1)

        receipt = cart.print_receipt()

        assert receipt[0] == "banana - 1 - €1.10"
        assert receipt[1] == "kiwi - 1 - €3.00"

    def test_total(self):
        cart = ShoppingCart()
        cart.add_item("banana", 2)
        cart.add_item("kiwi", 3)

        receipt = cart.print_receipt()

        assert receipt[0] == "banana - 2 - €2.20"
        assert receipt[1] == "kiwi - 3 - €9.00"
        assert receipt[2] == "Total - €11.20"
