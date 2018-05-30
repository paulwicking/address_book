from address_book.address_book import Entry
from unittest import TestCase


class TestEntry(TestCase):
    def setUp(self):
        self.test_entry_name = "Bob Smith"
        self.test_entry = Entry(name=self.test_entry_name)

    def test_entry_must_have_a_name(self):
        with self.assertRaises(TypeError):
            Entry()

    def test_entry_can_have_an_address(self):
        test_address = {'Street 1': 'Some street 1',
                        'Street 2': 'Some more info',
                        'Postal code': 12345,
                        'City': 'Test City',
                        'Country': 'Test Country'}
        test_entry_with_address = Entry(self.test_entry_name, address=test_address)

        result = test_entry_with_address.address
        self.assertEqual(test_address, result)

    def test_entry_can_have_a_phone_number(self):
        test_phone_number = "555-1234"
        test_entry_with_phone_number = Entry(
            self.test_entry_name, phone_number=test_phone_number)

        result = test_entry_with_phone_number.phone_number
        self.assertEqual(test_phone_number, result)

    def test_entry_can_have_email_address(self):
        test_email = "test@example.com"
        test_entry_with_email = Entry(self.test_entry_name, email=test_email)

        self.assertEqual(test_entry_with_email.email, test_email)

    def test_entry_can_have_multiple_phone_numbers(self):
        test_email = "test@example.com"
        another_test_email = "another_test@example.com"

        test_entry_with_multiple_email_addresses = Entry(
            self.test_entry_name,
            email=[test_email, another_test_email]
        )

        expected = [str(test_email), str(another_test_email)]
        result = test_entry_with_multiple_email_addresses.email

        self.assertEqual(expected, result)

    def test_entry_can_have_multiple_addresses(self):
        test_address1 = {'Street 1': 'Some street 1',
                         'Street 2': 'Some more info',
                         'Postal code': 12345,
                         'City': 'Test City',
                         'Country': 'Test Country'}

        test_address2 = {'Street 1': 'Another street 1',
                         'Street 2': 'Even more info',
                         'Postal code': 67890,
                         'City': 'Different Test City',
                         'Country': 'Another Test Country'}

        test_entry_with_multiple_addresses = Entry(
            self.test_entry_name,
            address=[test_address1, test_address2]
        )

        expected = [test_address1, test_address2]
        result = test_entry_with_multiple_addresses.address

        self.assertEqual(expected, result)

    def test_entry_name_is_composed_of_first_and_last_name(self):
        test_name = {"first_name": "John",
                     "last_name": "Smith",
                     }
        test_person = Entry(test_name)

        expected_full_name = "John Smith"
        result = test_person.name

        self.assertEqual(expected_full_name, result)

    def test_that__repr_returns_the_name_of_the_entry(self):
        result = self.test_entry.__repr__()

        self.assertEqual(result, self.test_entry.name)

    def test_that_entry_can_contain_organization_name(self):
        test_entry = Entry(name="John Doe", organization="ACME")

        expected = "ACME"
        result = test_entry.organization

        self.assertEqual(result, expected)

    def test_entries_automatically_get_a_uuid(self):
        uuid = self.test_entry._uuid

        self.assertIsNotNone(uuid)
