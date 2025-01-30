# class to have 4 functions: addition, subtraction, multiplication, division.


class MyMath:
    """ A simple class for basic math functions """

    def addition(self, number1, number2):
        """
        Math function addition
        :param number1: can be interger or float
        :param number2: can be interger or float
        :return: sum of number1 and number2
        """
        """ if not type(number1) == int:
            number1 = int(number1)
        if not type(number2) == int:
            number2 = int(number2)

        if isinstance(number1, int) and isinstance(number2, int):
            return number1 + number2 """

        try:
            return number1 + number2
        except TypeError:
            raise TypeError("Wrong types")

    def subtraction(self, number1, number2):
        """
        Math function subtraction
        :param number1: can be interger or float
        :param number2: can be interger or float
        :return: difference of number 1 and number2
        """
        try:
            return number1 - number2
        except TypeError:
            raise TypeError("Wrong types")

    def multiplication(self, number1, number2):
        """
        Math function multiplication
        :param number1: can be interger or float
        :param number2: can be interger or float
        :return: product of number 1 and number2
        """
        try:
            return number1 * number2
        except TypeError:
            raise TypeError("Wrong types")

    def division(self, number1, number2):
        """
        Math function division
        :param number1: can be interger or float
        :param number2: can be interger or float
        :return: fraction of number 1 and number2
        """
        try:
            return number1 / number2
        except TypeError:
            raise TypeError("Wrong types")
