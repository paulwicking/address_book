"""A simple address book."""


class Person:
    def __init__(self, name, address=None, phone_number=None, email=None):
        self.name = name.title()
        self.address = address
        self.phone_number = phone_number
        self.email = email
