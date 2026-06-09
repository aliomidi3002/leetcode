class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        stack = []

        for char in s:
            #in case of starting
            if char in bracket:
                stack.append(char)
            #in case of ending
            elif stack and bracket[stack[-1]] == char:
                stack.pop()
            else:
                return False
        
        if not stack:
            return True
        return False


# Last elemnt inside the stack has the highest priority to end