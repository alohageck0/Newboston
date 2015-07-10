__author__ = 'royalfiish'


class Parent():
    def print_last_name(self):
        print("Last_Name")


class Child(Parent):
    def print_first_name(self):
        print("First_name")

    def print_last_name(self):
        print("New_last_name")


child = Child()
parent = Parent()

child.print_first_name()
child.print_last_name()

parent.print_last_name()
