from main import logger
from time import sleep
from math import sqrt


"""Exercise 3"""
logger.info('Completing task 3...')
sleep(2)


class Copulation:
    """A class, that allows you to perform various operations on integers"""

    def factorial(self, num: int) -> int:
        """A method, that allows you to calculate the factorial of an integer"""
        fac_result = 1

        for i in range(2, num + 1):
            fac_result *= i

        return fac_result

    def sum(self, num: int) -> int | float:
        """Method to calculate the sum of the first n integers"""
        sum_result = num * (num + 1) / 2
        return sum_result

    def test_prim(self, num: int) -> bool:
        """Method for checking the primality of a given integer"""
        i = 2
        while i <= sqrt(num):
            if num % i == 0:
                return False
            i += 1
        if num > 1:
            return True

    def test_prims(self, num1: int, num2: int) -> list[int]:
        """Method to check if two numbers are prime to each other"""
        simple_num = []
        for number in range(num1, num2 + 1):
            if number > 1:
                for i in range(2, number):
                    if (number % i) == 0:
                        break
                else:
                    simple_num.append(number)

        return simple_num

    def table_mult(self, num: int) -> None:
        """Method that creates and displays the multiplication table of the given integer"""
        for i in range(1, 11):
            print(num, 'x', i, '=', num * i)

    def all_table_mult(self) -> None:
        """Method to display all integer multiplication tables"""
        for i in range(1, 10):
            print(*range(i, i * 10, i), sep='\t')

    def list_div(self, num: int) -> list:
        """Method, that gets all divisors of the given number in a new list named Ldiv"""
        ldiv = [i for i in range(2, num + 1) if num % i == 0]

        return ldiv

    def list_div_prim(self, num: int) -> list:
        """Method, that gets all prime divisors of a given integer"""
        result = list(filter(lambda x: all(map(lambda i: x % i != 0, range(2, int(x ** 0.5) + 1))),
                             [i for i in range(2, num + 1) if num % i == 0]))

        return result


def main():
    some_num = Copulation()
    print(some_num.__doc__, '\n')

    fac_num = 5
    print(f'Factorial of a number {fac_num} = {some_num.factorial(fac_num)}')

    num_sum = 10
    print(f'The sum of the first integers from 1 to {num_sum} is {int(some_num.sum(num_sum))}')

    num_test_prime = 11
    print(f'Number {num_test_prime} - %s' % ('prime number' if some_num.test_prim(num_test_prime) else 'not prime'))

    num_1_test_prims = 1
    num_2_test_prims = 17
    print(f'Prime numbers in the range '
          f'{num_1_test_prims} to {num_2_test_prims} - {some_num.test_prims(num_1_test_prims, num_2_test_prims)}')

    num_table_mult = 2
    print(f'Multiplication table of number {num_table_mult}')
    some_num.table_mult(num_table_mult)

    print('Multiplication table for all numbers from 1 to 9')
    some_num.all_table_mult()

    print(some_num.list_div(24))

    print(some_num.list_div_prim(9990))


main()
