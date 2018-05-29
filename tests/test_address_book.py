from unittest import TestCase
from address_book.address_book import AddressBook, Entry


class TestAddressBook(TestCase):
    def setUp(self):
        self.address_book = AddressBook()

        self.assertIsInstance(self.address_book, AddressBook)

    def test_can_add_entry_to_address_book(self):
        test_person = Entry("John Doe")

        self.address_book.add_entry(test_person)

    def test_can_list_entries_in_address_book(self):
        test_person_1 = Entry("John Doe")
        test_person_2 = Entry("Jane Doe")

        self.address_book.add_entry(test_person_1)
        self.address_book.add_entry(test_person_2)

        expected = [test_person_1, test_person_2]
        result = self.address_book.get_entries()

        self.assertEqual(expected, result)
