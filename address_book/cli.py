"""Command Line Interface module for address book."""


class CLI:
    def __init__(self):
        pass

    def display_entries(self, address_book):
        for entry in address_book.get_entries():
            print(entry.name)
