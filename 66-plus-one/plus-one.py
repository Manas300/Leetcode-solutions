class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(map(str, digits)))  # Join digits to form number
        num += 1                              # Add 1
        return [int(d) for d in str(num)]  

        