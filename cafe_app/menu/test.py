import sys

sys.path.append('.\\')

import unittest
from cafe_app.menu.models import Menu, Category
from cafe_app.extensions import db


class MenuTest(unittest.TestCase):
    def setUp(self):
        self.item1 = Menu("cake", 200, "This is cake", 1, "cake1.jpg", False)

    def test_creation_order(self):
        self.assertEqual(self.item1.name, "cake")
        self.assertEqual(self.item1.price, 200)
        self.assertEqual(self.item1.description, "This is cake")
        self.assertEqual(self.item1.category_id, 1)
        self.assertEqual(self.item1.picture_path, "cake1.jpg")
        self.assertEqual(self.item1.status, False)
        self.assertIsInstance(self.item1, db.Model)


class CategoryTest(unittest.TestCase):
    def setUp(self):
        self.cat1 = Category("Category1", "This is first Cat.")

    def test_creation_order(self):
        self.assertEqual(self.cat1.name, "Category1")
        self.assertEqual(self.cat1.description, "This is first Cat.")
        self.assertIsInstance(self.cat1, db.Model)


if __name__ == '__main__':
    unittest.main()
