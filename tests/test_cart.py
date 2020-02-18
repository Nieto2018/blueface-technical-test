from shoppingcart.cart import ShoppingCart

import unittest


class TestCartMethods(unittest.TestCase):

    def test_add_item(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1)

        receipt = cart.print_receipt()

        assert receipt[0] == "apple - 1 - €1.00"
        assert receipt[1] == "Total - €1.00"

    def test_add_item_with_multiple_quantity(self):
        cart = ShoppingCart()
        cart.add_item("apple", 2)

        receipt = cart.print_receipt()

        assert receipt[0] == "apple - 2 - €2.00"
        assert receipt[1] == "Total - €2.00"

    def test_add_different_items(self):
        cart = ShoppingCart()
        cart.add_item("banana", 1)
        cart.add_item("kiwi", 1)

        receipt = cart.print_receipt()

        assert receipt[0] == "banana - 1 - €1.10"
        assert receipt[1] == "kiwi - 1 - €3.00"
        assert receipt[2] == "Total - €4.10"

    def test_total_with_wrong_currency(self):
        # Default currency is EUR
        cart = ShoppingCart('xxx')
        cart.add_item("banana", 2)

        receipt = cart.print_receipt()

        assert receipt[0] == "banana - 2 - €2.20"
        assert receipt[1] == "Total - €2.20"

    def test_total_in_eur(self):
        cart = ShoppingCart()
        cart.add_item("banana", 2)
        cart.add_item("kiwi", 3)

        receipt = cart.print_receipt()

        assert receipt[0] == "banana - 2 - €2.20"
        assert receipt[1] == "kiwi - 3 - €9.00"
        assert receipt[2] == "Total - €11.20"

    def test_total_in_usd(self):
        cart = ShoppingCart('usd')
        cart.add_item("banana", 2)
        cart.add_item("kiwi", 3)

        receipt = cart.print_receipt()

        assert receipt[0] == "banana - 2 - $2.42"
        assert receipt[1] == "kiwi - 3 - $9.90"
        assert receipt[2] == "Total - $12.32"

    def test_total_in_gbp(self):
        cart = ShoppingCart('gbp')
        cart.add_item("banana", 2)
        cart.add_item("kiwi", 3)

        receipt = cart.print_receipt()

        assert receipt[0] == "banana - 2 - £2.79"
        assert receipt[1] == "kiwi - 3 - £11.43"
        assert receipt[2] == "Total - £14.22"
