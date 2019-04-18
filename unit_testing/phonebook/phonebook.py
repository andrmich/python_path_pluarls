class Phonebook:

    def __init__(self):
        self.entries = {}

    def add(self, name, number):
        if name in self.entries.keys():
            raise KeyError('This name is already in the phonebook.')
        elif number in self.entries.values():
            raise KeyError('This number is already in the phonebook.')
        self.entries[name] = number

    def lookup(self, name):
        return self.entries[name]

    def is_consistent(self):
        return True