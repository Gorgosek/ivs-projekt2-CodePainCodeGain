"""! @brief BRIEF DESCRIPTION OF THE FILE. (will be on top of the file page)"""


##
# @mainpage MAIN PAGE NAME (use only with the main)
#
# @section description_main SECTION NAME
# SECTION DESCRIPTION
#
# Copyright (c) CodePainCodeGain.  All rights reserved.


##
# @file doxy_example.py
#
# @brief BRIEF DESCRIPTION OF FILE
#
# @section description_file SECTION NAME
# - SECTION DESCRIPTION
#
# @section libraries_main Libraries/Modules
# USED LIBRARIES IN FILE
#
# @section notes_file Notes
# NOTES DESCRIPTION
#
# @section author_file Author(s)
# AUTHOR(S) NAME(S)


# Imports
import random
import doxy_example_other

# Global Constants
## A = 1, min number of sth
A = 1
## B = 1, number representing ...
B = 1

#Classes
class ClassName:
    """! CLASS DESCRIPTION IN CLASS LIST.

    DETAILED CLASS DESCRIPTION.
    """

    def __init__(self, name):
        """! The ClassName initializer.

        @param name  NAME.

        @return  An instance of the class initialized with the specified name.
        """

        ## The name.
        self.name = name
        ## The value.
        self.value = random.randint(0, 50)

    def __str__(self):
        """! Retrieves ClassMember description.

        @return  A description of the instance.
        """

        return f"The {self.name} has a value of {self.value}."


# Functions
def init():
    """! Initializes the program.
    """
    print("Initializing program")


def function_example(parameterOne, paramTwo):
    """! FUNCTION DESCRIPTION

    @param parameterOne  DESCRIPTION.
    @param paramTwo      DESCRIPTION.

    @return  RETURN.
    """
    number = parameterOne + paramTwo
    return number


def main():
    """! Main program entry."""

    init()  # program initialization
    c = function_example(1, 2) + function_example(3)
    print(c)


if __name__ == "__main__":
    main()
