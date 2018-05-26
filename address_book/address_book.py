"""A simple address book."""


class Person:
    def __init__(self, name, address=None, phone_number=None):
        self.name = name
        self.address = address
        self.phone_number = phone_number
