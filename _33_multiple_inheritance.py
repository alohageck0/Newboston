__author__ = 'royalfiish'

class Parent():

    def print_last_name(self):
        print("Last_Name")

class Sibling():

    def toy(self):
        print("I have toy")

class Child(Parent, Sibling):

    def print_first_name(self):
        print("First_name")

    def print_last_name(self):
        print("New_last_name")

child = Child()


child.print_first_name()
child.print_last_name()
child.toy()