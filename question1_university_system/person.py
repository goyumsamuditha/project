class Person:  # Abstract base class for all persons in the university
    def __init__(self, name):
        self.name = name

    def get_responsibilities(self):  # method to be overridden in subclasses
        return "General university member"  # default responsibility


class Staff(Person):
    def get_responsibilities(self):  # override to specify staff responsibilities
        return "Support university operations"