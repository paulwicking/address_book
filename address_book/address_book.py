"""A simple address book."""


class Person:
    def __init__(self, name, address=None, phone_number=None, email=None):
        self.name, self.first_name, self.last_name = None, None, None
        self._parse_name(name)

        self.address = address
        self.phone_number = phone_number
        self.email = email

    def _parse_name(self, name):
        """
        Parse whatever is passed as ``name`` and update ``self.name`` from that.

        :param name: A person's name as string or dictionary.
        :return: The method doesn't return anything.
        """
        if type(name) == str:
            names_as_list = name.split()
            self.first_name = names_as_list[0].title()
            self.last_name = names_as_list[-1].title()
        elif type(name) == dict:
            self.first_name = name["first_name"].title()
            self.last_name = name["last_name"].title()

        self.name = self.first_name + " " + self.last_name
