class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1:
            return s

        longpd = s[0]

        for i in range(len(s)):

            # odd length  (center = one char)
            left, right = i - 1, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if len(longpd) < right - left + 1:
                    longpd = s[left:right+1]
                left  -= 1
                right += 1

            # even length  (center = between two chars)
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if len(longpd) < right - left + 1:
                    longpd = s[left:right+1]
                left  -= 1
                right += 1

        return longpd
