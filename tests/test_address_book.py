from unittest import TestCase
from address_book.address_book import AddressBook


class TestAddressBook(TestCase):
    def test_can_create_an_address_book(self):
        address_book = AddressBook()

        self.assertIsInstance(address_book, AddressBook)
