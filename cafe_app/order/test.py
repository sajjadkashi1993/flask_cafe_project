import sys
import unittest
from cafe_app.order.models import Order, Cart, Receipt
from cafe_app.extensions import db
from datetime import datetime

sys.path.append('.\\')


class OrderTest(unittest.TestCase):
    def setUp(self):
        self.order1 = Order(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "Tehran, Street1", "Very Good!", "in_process",
                            "2", "3", "4", "order_ahead")

    def test_creation_order(self):
        self.assertTrue(datetime.strptime(self.order1.order_time, "%d/%m/%Y %H:%M:%S"))
        self.assertEqual(self.order1.delivery_address, "Tehran, Street1")
        self.assertEqual(self.order1.comment, "Very Good!")
        self.assertEqual(self.order1.state, "in_process")
        self.assertEqual(self.order1.reserved_id, "2")
        self.assertEqual(self.order1.receipt_id, "3")
        self.assertEqual(self.order1.offer_id, "4")
        self.assertEqual(self.order1.order_type, "order_ahead")
        self.assertIsInstance(self.order1, db.Model)


class CartTest(unittest.TestCase):
    def setUp(self):
        self.cart1 = Cart('{"id": 1, "quantity": 2}', 1, 10)

    def test_creation_order_item(self):
        self.assertEqual(self.cart1.item_quantity, '{"id": 1, "quantity": 2}')
        self.assertEqual(self.cart1.order_id, 1)
        self.assertEqual(self.cart1.customer_id, 10)
        self.assertIsInstance(self.cart1, db.Model)


class ReceiptTest(unittest.TestCase):
    def setUp(self):
        self.receipt1 = Receipt(101.51, 43, 120.10, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    def test_creation_receipt(self):
        self.assertEqual(self.receipt1.total_price, 101.51)
        self.assertEqual(self.receipt1.discount, 43)
        self.assertEqual(self.receipt1.final_price, 120.10)
        self.assertTrue(datetime.strptime(self.receipt1.receipt_time, "%d/%m/%Y %H:%M:%S"))
        self.assertIsInstance(self.receipt1, db.Model)


if __name__ == '__main__':
    unittest.main()
