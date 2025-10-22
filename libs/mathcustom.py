from math import isqrt


class MathCustom:
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
