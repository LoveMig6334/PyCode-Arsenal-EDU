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

    @staticmethod
    def gcd(a: int, b: int) -> int:
        """Return the greatest common divisor of two integers."""
        while b:
            a, b = b, a % b
        return abs(a)

    @staticmethod
    def least_common_multiple(a: int, b: int) -> int:
        """Return the least common multiple of two integers."""

        return abs(a * b) // MathDCustom.gcd(a, b)


if __name__ == "__main__":
    print(MathDCustom.is_prime(29))  # True
    print(MathDCustom.prime_factorize(315))  # [3, 3, 5, 7]
    print(MathDCustom.gcd(48, 18))  # 6
    print(MathDCustom.least_common_multiple(4, 9))  # 36
