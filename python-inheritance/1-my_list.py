#!/usr/bin/python3
"""
This is a module is named 1-my_list

Todo:
    Create a class MyList
    Create a method named print_sorted(self)
"""


class MyList(list):
    """
    This is MyList class inherits from list

    Args:
        No Arguments
    """

    def print_sorted(self):
        """
        Print_sorted method prints sort integers in
        MyList

        Args:
            self(MyList): the list of integr

        Return: Nothing
        """
        sorted_list = sorted(self)
        print(sorted_list)
