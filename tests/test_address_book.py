from unittest import TestCase
from address_book.address_book import AddressBook, Person


class TestAddressBook(TestCase):
    def setUp(self):
        self.address_book = AddressBook()

        self.assertIsInstance(self.address_book, AddressBook)

    def test_can_add_entry_to_address_book(self):
        test_person = Person("John Doe")

        self.address_book.add_entry(test_person)
