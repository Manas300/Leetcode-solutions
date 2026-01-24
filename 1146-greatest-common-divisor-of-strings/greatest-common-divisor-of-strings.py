class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Must be compatible repeats of the same base pattern
        if str1 + str2 != str2 + str1:
            return ""

        # Euclidean algorithm for gcd (no libraries)
        a, b = len(str1), len(str2)
        while b != 0:
            a, b = b, a % b

        return str1[:a]
