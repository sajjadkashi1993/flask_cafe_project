from unittest import TestCase
import unittest
from cafe_app.user.models import User
from hashlib import sha256
from cafe_app.extensions import db


class UserTest(TestCase):
    def setUp(self):
        self.u1 = User("first_name", "last_name", "email@i.iu", "password", 'address', "09123456789", 'user')

    def test_creation_User(self):
        self.assertEqual(self.u1.f_name, "first_name")
        self.assertEqual(self.u1.l_name, "last_name")
        self.assertEqual(self.u1.email, "email@i.iu")
        self.assertEqual(self.u1.password, sha256("password".encode()).hexdigest())
        self.assertEqual(self.u1.address, "address")
        self.assertEqual(self.u1.phone_number, "09123456789")
        self.assertIsInstance(self.u1, db.Model)

    def test_find(self):
        user = self.u1.find('3')
        self.assertIsInstance(user, list)

    def test_login(self):
        login = self.u1.login('3', "12345")
        self.assertEqual(login, False)


if __name__ == '__main__':
    unittest.main()
