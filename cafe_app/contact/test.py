from unittest import TestCase
import unittest
from cafe_app.contact.models import Contact
from cafe_app.extensions import db
from cafe_app.core.exceptions import NameValidationError, EmailValidationError, PhoneValidationError


class ContactTest(TestCase):
    def setUp(self):
        self.c1 = Contact("first_name", "last_name", "email@i.iu", "09010332231", "That's greats")

    def test_creation_Contact(self):
        self.assertEqual(self.c1.first_name, "first_name")
        self.assertEqual(self.c1.last_name, "last_name")
        self.assertEqual(self.c1.email, "email@i.iu")
        self.assertEqual(self.c1.phone, "09010332231")
        self.assertEqual(self.c1.message, "That's greats")
        self.assertIsInstance(self.c1, db.Model)

    def test_validation(self):
        self.assertRaises(NameValidationError, Contact, "Am", "hassani", "email@i.iu", "09010332241", "Wow!!!")
        self.assertRaises(NameValidationError, Contact, "Amir2", "hassani", "email@i.iu", "09010332241", "Wow!!!")
        self.assertRaises(NameValidationError, Contact, "Hamidreza", "Ah", "email@i.iu", "09010332231", "That's great")
        self.assertRaises(NameValidationError, Contact, "Hamidreza", "Ahadian2", "email@i.iu", "09010332231",
                          "That's great")
        self.assertRaises(NameValidationError, Contact, "Sajjad", "Kashi", "email@gamil.coom", "09010332241", "Wow!!!")
        self.assertRaises(NameValidationError, Contact, "Sajjad", "Kashi", "emailgamil.com", "09010332241", "Wow!!!")
        self.assertRaises(NameValidationError, Contact, "Sajjad", "Kashi", "email@.gamil.com", "09010332241", "Wow!!!")
        self.assertRaises(NameValidationError, Contact, "Sajjad", "Kashi", "email@gamilcm", "09010332241", "Wow!!!")
        self.assertRaises(EmailValidationError, Contact, "sajjad", "hassani", "emailigmail@.com", "09010332251",
                          "It's the best coffee")
        self.assertRaises(NameValidationError, Contact, )
        self.assertRaises(PhoneValidationError, Contact, "erfan", "jamshidi", "email@i.iu", "0901033224", "Not bad")
        self.assertRaises(PhoneValidationError, Contact, "erfan", "jamshidi", "email@i.iu", "90103322412", "Not bad")
        self.assertRaises(PhoneValidationError, Contact, "erfan", "jamshidi", "email@i.iu", "+9890103322318", "Not bad")
        self.assertRaises(PhoneValidationError, Contact, "erfan", "jamshidi", "email@i.iu", "+988010332231", "Not bad")
        self.assertRaises(PhoneValidationError, Contact, "erfan", "jamshidi", "email@i.iu", "+989-10332231", "Not bad")
        self.assertRaises(PhoneValidationError, Contact, "erfan", "jamshidi", "email@i.iu", "+989a10332231", "Not bad")


if __name__ == '__main__':
    unittest.main()
