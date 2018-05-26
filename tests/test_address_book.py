from address_book.address_book import Person
from unittest import main, TestCase


class TestAddressBook(TestCase):
    def setUp(self):
        self.test_person_name = "Bob Smith"
        self.test_person = Person(name=self.test_person_name)

    def test_person_must_have_a_name(self):
        with self.assertRaises(TypeError):
            Person()

    def test_person_can_have_an_address(self):
        test_person_address = {'Street 1': 'Some street 1',
                               'Street 2': 'Some more info',
                               'Postal code': 12345,
                               'City': 'Test City',
                               'Country': 'Test Country'}
        test_person_with_address = Person(self.test_person_name, test_person_address)

        result = test_person_with_address.address
        assert result == test_person_address

    def test_person_can_have_a_phone_number(self):
        test_person_phone_number = "555-1234"
        test_person_with_phone_number = Person(
            self.test_person_name, phone_number=test_person_phone_number)

        result = test_person_with_phone_number.phone_number
        assert result == test_person_phone_number


if __name__ == '__main__':
    main()
