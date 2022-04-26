import unittest

from phonebook.phonebook import PhoneBook


class PhoneBookTest(unittest.TestCase):
    def setUp(self) -> None:
        self.phonebook = PhoneBook()

    def tearDown(self) -> None:
        pass

    def test_lookup_by_name(self):
        self.phonebook.add("Test 0", "12345")
        number = self.phonebook.lookup("Test 0")
        self.assertEqual("12345", number)

    def test_missing_name(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistant())

    def test_is_consistent_with_different_entries(self):
        self.phonebook.add("Test 0", "12345")
        self.phonebook.add("Test 1", "012345")
        self.assertTrue(self.phonebook.is_consistant())

    def test_inconsistant_with_duplicate_enteries(self):
        self.phonebook.add("Test 0", "12345")
        self.phonebook.add("Test 1", "12345")
        self.assertFalse(self.phonebook.is_consistant())

    def test_incosistant_with_duplicat_prefix(self):
        self.phonebook.add("Test 0", "12345")
        self.phonebook.add("Test 1", "123")
        self.assertFalse(self.phonebook.is_consistant())

    def test_phonebook_adds_names_and_numbers(self):
        self.phonebook.add("Test 0", "12345")
        self.assertIn("Test 0", self.phonebook.get_names())
        self.assertIn("12345", self.phonebook.get_numbers())
