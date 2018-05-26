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

    def test_person_can_have_an_address(self):
        test_person_name = "Bob Smith"
        test_person_address = {'Street 1': 'Some street 1',
                               'Street 2': 'Some more info',
                               'Postal code': 12345,
                               'City': 'Test City',
                               'Country': 'Test Country'}
        test_person = address_book.Person(test_person_name, test_person_address)

        result = test_person.address
        assert result == test_person_address

    def test_person_can_have_a_phone_number(self):
        test_person_name = "Bob Smith"
        test_person_phone_number = "555-1234"
        test_person = address_book.Person(test_person_name, phone_number=test_person_phone_number)

        result = test_person.phone_number
        assert result == test_person_phone_number


if __name__ == '__main__':
    main()