from unittest import TestCase
from address_book.address_book import AddressBook, Person


class TestAddressBook(TestCase):
    def test_can_create_an_address_book(self):
        address_book = AddressBook()

        self.assertIsInstance(address_book, AddressBook)

    def test_can_add_entry_to_address_book(self):
        address_book = AddressBook()
        test_parson = Person("John Doe")

        address_book.add_entry(test_parson)
