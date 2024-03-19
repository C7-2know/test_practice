class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        if self.quantity<0:
            raise ValueError()
        return self.price * self.quantity


class ShoppingCart:
    def init(self):
        self.cart = []

    def add_product(self, product):
        self.cart.append(product)

    def get_cart_total(self):
        total = 0
        for product in self.cart:
            total += product.calculate_price()
        return total  
     
import unittest

# Unit test

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product("Laptop", 999.99, 5)

    def test_attributes(self):
        self.assertEqual(self.product.name, "Laptop")
        self.assertEqual(self.product.price, 999.99)
        self.assertEqual(self.product.quantity, 5)

    def test_total_price(self):
        self.assertEqual(self.product.total_price(), 999.99 * 5)
    def test_total_price_zero_quantity(self):
        # Test total price when quantity is zero
        zero_quantity_product = Product("Mouse", 19.99, 0)
        self.assertEqual(zero_quantity_product.total_price(), 0)


    def test_total_price_negative_quantity(self):
        # Test total price when quantity is negative
        negative_quantity_product = Product("Headphones", 49.99, -1)
        with self.assertRaises(ValueError):
            negative_quantity_product.total_price()

class TestShoppingCart(unittest.TestCase):
    
        

    def test_get_cart_total_with_empty_cart(self):
        # Test calculating total price with an empty cart
        cart = ShoppingCart()
        self.assertEqual(cart.get_cart_total(), 0)

    def test_get_cart_total_with_products(self):
        # Test calculating total price with products in the cart
        product1 = Product("Laptop", 999.99, 1)
        product2 = Product("Phone", 599.99, 2)

        # Add products to the cart
        Cart=ShoppingCart()
        Cart.add_product(product1)
        Cart.add_product(product2)

        # Calculate total price
        expected_total = product1.total_price() + product2.total_price()
        self.assertEqual(Cart.get_cart_total(), expected_total)



if __name__ == "__main__":
    unittest.main()

    
