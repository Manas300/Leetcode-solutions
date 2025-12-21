class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")": "(", "}": "{", "]": "["}

        for ch in s:
            if ch in brackets.values():   # opening brackets
                stack.append(ch)
            elif ch in brackets:          # closing brackets
                if not stack or stack[-1] != brackets[ch]:
                    return False
                stack.pop()

        return not stack

            
