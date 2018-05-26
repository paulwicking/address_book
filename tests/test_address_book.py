from address_book import address_book
from unittest import main, TestCase


class TestAddressBook(TestCase):
    def test_can_import_address_book(self):
        import address_book

    def test_can_create_a_person(self):
        test_person = address_book.Person('test')

        assert test_person is not None

    def test_person_can_have_a_name(self):
        test_person_name = "Bob Smith"
        test_person = address_book.Person(name=test_person_name)

        result = test_person.name

        assert result == test_person_name


if __name__ == '__main__':
    main()