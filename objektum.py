class Employee:
    """ Ez egy osztalyt hoz letre. """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

john = Employee("John Doe", 30)
print(john.get_name())
