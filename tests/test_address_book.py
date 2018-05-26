from address_book import address_book
from unittest import main, TestCase


class TestAddressBook(TestCase):
    def test_can_import_address_book(self):
        import address_book

    def test_can_create_a_person(self):
        person = address_book.Person()

        assert person is not None


if __name__ == '__main__':
    main()