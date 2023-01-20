import sys
import unittest
from cafe_app.offer.models import Offer
from cafe_app.extensions import db
from datetime import datetime

sys.path.append('.\\')


class OfferTest(unittest.TestCase):
    def setUp(self):
        self.offer1 = Offer(50, 40, "off40")

    def test_creation_order(self):
        self.assertEqual(self.offer1.min_price, 0)
        self.assertEqual(self.offer1.max_price, 50)
        self.assertEqual(self.offer1.percent, 40)
        self.assertIsInstance(self.offer1.expire_time, datetime)
        self.assertEqual(self.offer1.expire_count, 1)
        self.assertIsInstance(self.offer1, db.Model)


if __name__ == '__main__':
    unittest.main()
