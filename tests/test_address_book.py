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
        self.assertEqual(test_person_address, result)

    def test_person_can_have_a_phone_number(self):
        test_person_phone_number = "555-1234"
        test_person_with_phone_number = Person(
            self.test_person_name, phone_number=test_person_phone_number)

        result = test_person_with_phone_number.phone_number
        self.assertEqual(test_person_phone_number, result)

    def test_names_are_title_cased(self):
        test_person = Person("john smith")
        expected_name = "John Smith"
        actual_name = test_person.name

        self.assertEqual(expected_name, actual_name)

    def test_person_can_have_email_address(self):
        test_person_email = "test@example.com"
        test_person_with_email = Person(self.test_person_name, email=test_person_email)

        self.assertEqual(test_person_with_email.email, test_person_email)

    def test_person_can_have_multiple_phone_numbers(self):
        test_email = "test@example.com"
        another_test_email = "another_test@example.com"

        test_person_with_multiple_email_addresses = Person(
            self.test_person_name,
            email=[test_email, another_test_email]
        )

        expected = [str(test_email), str(another_test_email)]
        result = test_person_with_multiple_email_addresses.email

        self.assertEqual(expected, result)

    def test_test_person_can_have_multiple_addresses(self):
        test_person_address1 = {'Street 1': 'Some street 1',
                                'Street 2': 'Some more info',
                                'Postal code': 12345,
                                'City': 'Test City',
                                'Country': 'Test Country'}

        test_person_address2 = {'Street 1': 'Another street 1',
                                'Street 2': 'Even more info',
                                'Postal code': 67890,
                                'City': 'Different Test City',
                                'Country': 'Another Test Country'}

        test_person_with_multiple_addresses = Person(
            self.test_person_name,
            address=[test_person_address1, test_person_address2]
        )

        expected = [test_person_address1, test_person_address2]
        result = test_person_with_multiple_addresses.address

        self.assertEqual(expected, result)

    def test_persons_name_is_composed_of_first_and_last_name(self):
        test_name = {"first_name": "john",
                     "last_name": "smith",
                     }
        test_person = Person(test_name)

        expected_full_name = "John Smith"
        result = test_person.name

        self.assertEqual(expected_full_name, result)

    def test_passing_name_as_string_sets_first_and_last_name(self):
        test_person_name = "John Doe"
        test_person = Person(test_person_name)

        expected_first_name = "John"
        expected_last_name = "Doe"

        actual_first_name = test_person.first_name
        actual_last_name = test_person.last_name

        self.assertEqual(expected_first_name, actual_first_name)
        self.assertEqual(expected_last_name, actual_last_name)


if __name__ == '__main__':
    main()
