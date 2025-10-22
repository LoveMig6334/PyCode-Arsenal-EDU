from math import isqrt


class MathDCustom:
    @staticmethod
    def is_prime(num: int) -> bool:
        """Check if a number is prime."""

        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False

        limit = isqrt(num)
        i = 5
        while i <= limit:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6

        return True

    @staticmethod
    def prime_factorize(num) -> list:
        """
        A Function to return the prime factorization of a given number.
        """

        factors = []
        while num % 2 == 0:
            factors.append(2)
            num //= 2

        for i in range(3, isqrt(num) + 1, 2):
            while num % i == 0:
                factors.append(i)
                num //= i

        if num > 2:
            factors.append(num)

        return factors
