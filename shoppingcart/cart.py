import json
import typing

from . import abc

CURRENCIES = {
    "eur": [1, "€%.2f"],
    "usd": [1.1, "$%.2f"],
    "gbp": [1.27, "£%.2f"]
}


class ShoppingCart(abc.ShoppingCart):
    def __init__(self, currency_code: str = "eur"):
        # With Python 3.7 the built-in dict class gained the ability to remember insertion order
        # In previous version of python you should use OrderedDict objects
        # https://docs.python.org/3.7/library/collections.html#collections.OrderedDict
        self._items = dict()

        self._products = self._get_products()
        self._set_currency(currency_code)

    def _set_currency(self, currency_code):
        if currency_code in CURRENCIES.keys():
            self._currency = currency_code
        else:
            # Default currency EUR
            self._currency = 'eur'

    def _get_products(self):
        products = {}

        try:
            with open("../products.json") as file:
                data = json.load(file)
                for product in data['products']:
                    name = product['name']
                    price = product['price']
                    products[name] = price
        except FileNotFoundError:
            print("The product file not found")
        except:
            print("Error opening the file")

        return products

    def print_receipt(self) -> typing.List[str]:
        lines = []
        total_price = 0

        for item in self._items.items():
            price = self._get_product_price(item[0]) * item[1]
            total_price = total_price + price

            price_string = self._get_price_by_currency(price)

            lines.append(item[0] + " - " + str(item[1]) + ' - ' + price_string)

        total_price_string = self._get_price_by_currency(total_price)
        lines.append('Total - ' + total_price_string)

        return lines

    def add_item(self, product_code: str, quantity: int):
        # To avoid that an item appears in the item list if it is not in the product list
        if product_code not in self._products.keys():
            raise Exception("The selected product is not in the product list")

        if product_code not in self._items:
            self._items[product_code] = quantity
        else:
            q = self._items[product_code]
            self._items[product_code] = q + quantity

    def _get_product_price(self, product_code: str) -> float:
        price = 0.0

        if product_code in self._products.keys():
            price = self._products[product_code]

        return price

    def _get_price_by_currency(self, price: float) -> str:
        currency = CURRENCIES[self._currency]

        currency_price = price * currency[0]
        currency_price_string = currency[1] % currency_price

        return currency_price_string
