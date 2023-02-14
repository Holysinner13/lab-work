from main import logger
from time import sleep
from math import sqrt


"""Exercise 3"""
logger.info('Completing task 3...')
sleep(2)


class Copulation:
    """A class, that allows you to perform various operations on integers"""

    def factorial(self, num):
        """A method, that allows you to calculate the factorial of an integer"""
        result = 1

        for i in range(2, num + 1):
            result *= i

        return f'Factorial of a number {num} = {result}'

    def sum(self, num):
        """Method to calculate the sum of the first n integers"""
        result = num * (num + 1) / 2
        return f'The sum of the first integers from 1 to {num} is {int(result)}'

    def test_prim(self, num):
        """Method for checking the primality of a given integer"""
        i = 2
        while i <= sqrt(num):
            if num % i == 0:
                return f'Number {num} - not prime'
            i += 1
        if num > 1:
            return f'Number {num} - prime number'

    def test_prims(self, num1, num2):
        """Method to check if two numbers are prime to each other"""
        simple_num = []
        for number in range(num1, num2 + 1):
            if number > 1:
                for i in range(2, number):
                    if (number % i) == 0:
                        break
                else:
                    simple_num.append(number)

        return f'Prime numbers in the range {num1} to {num2} - {simple_num}'

    def table_mult(self, num):
        """Method that creates and displays the multiplication table of the given integer"""
        print(f'Multiplication table of number {num}')
        for i in range(1, 11):
            print(num, 'x', i, '=', num * i)

    def all_table_mult(self):
        """Method to display all integer multiplication tables"""
        print('Multiplication table for all numbers from 1 to 9')
        for i in range(1, 10):
            print(*range(i, i * 10, i), sep='\t')

    def list_div(self, num):
        """Method, that gets all divisors of the given number in a new list named Ldiv"""
        ldiv = [i for i in range(2, num + 1) if num % i == 0]

        return ldiv

    def list_div_prim(self, num):
        """Method, that gets all prime divisors of a given integer"""
        result = list(filter(lambda x: all(map(lambda i: x % i != 0, range(2, int(x ** 0.5) + 1))),
                             [i for i in range(2, num + 1) if num % i == 0]))

        return result


some_num = Copulation()
print(some_num.__doc__, '\n')
print(some_num.factorial(5))
print(some_num.sum(10))
print(some_num.test_prim(8))
print(some_num.test_prims(1, 17))
some_num.table_mult(2)
some_num.all_table_mult()
print(some_num.list_div(24))
print(some_num.list_div_prim(9990))
print()
