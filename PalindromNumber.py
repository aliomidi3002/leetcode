class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        forward = len(str(x)) - 1
        backward = 0
        x_str = str(x)
        while forward > backward:
            if x_str[forward] != x_str[backward]:
                return False
            forward -= 1
            backward += 1
        return True