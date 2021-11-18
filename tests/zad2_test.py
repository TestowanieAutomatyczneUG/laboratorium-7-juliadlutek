import unittest
from src.zad2 import ValidPassword

class ValidPasswordTest(unittest.TestCase):
    def setUp(self):
        self.temp = ValidPassword()

    def test_valid_password(self):
        self.assertEqual(self.temp.func("ValidPasword$123"), True)

    def test_passwd_without_special(self):
        self.assertFalse(self.temp.func("Password12345"))

    def test_too_short_passwd(self):
        self.assertFalse(self.temp.func("Pass#1"))

    def test_passwd_without_cap(self):
        self.assertFalse(self.temp.func("password12345:)"))

    def test_passwd_without_number(self):
        self.assertFalse(self.temp.func("Password!"))

    def test_too_short_without_cap(self):
        self.assertFalse(self.temp.func("pas1$"))

    def test_too_short_without_special(self):
        self.assertFalse(self.temp.func("Pas11"))

    def test_too_short_without_number(self):
        self.assertFalse(self.temp.func("Pas$$"))

    def test_empty_string(self):
        self.assertFalse(self.temp.func(''))

    def test_not_string(self):
        with self.assertRaises(ValueError):
            self.temp.func(53.67)