

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []   # stores all valid combinations
        path = []     # current building string as a list of characters

        def backtrack(open_count, close_count):
            # If we have used all 2*n parentheses, save the result
            if len(path) == 2 * n:
                result.append("".join(path))  # convert list to string
                return

            # Choice 1: Add "(" if we still have opens left
            if open_count < n:
                path.append("(")                         # choose "("
                backtrack(open_count + 1, close_count)   # explore
                path.pop()                               # undo (backtrack)

            # Choice 2: Add ")" only if it won't break validity
            if close_count < open_count:
                path.append(")")                         # choose ")"
                backtrack(open_count, close_count + 1)   # explore
                path.pop()                               # undo (backtrack)

        backtrack(0, 0)   # start with 0 open and 0 close used
        return result
