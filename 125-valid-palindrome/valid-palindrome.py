class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove non-alphanumeric characters and convert to lowercase
        filtered_s = "".join(char.lower() for char in s if char.isalnum())

        # Check if the filtered string is the same when reversed
        return filtered_s == filtered_s[::-1]  # Using slicing to reverse