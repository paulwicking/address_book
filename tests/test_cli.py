from unittest import mock, TestCase
from address_book.cli import CLI
from address_book.address_book import AddressBook, Entry


class TestCommandLineInterface(TestCase):

    def test_cli_prints_a_list_of_entries(self):
        test_book = AddressBook()
        test_book.add_entry(Entry(name="Test entry 1"))
        test_book.add_entry(Entry(name="Test entry 2"))

        cli = CLI()

        with mock.patch("builtins.print") as mock_print:
            cli.display_entries(test_book)

        self.assertEqual(mock_print.call_count, 2)
        # mock.assert_called_with() returns the final call
        mock_print.assert_called_with("Test entry 2")
