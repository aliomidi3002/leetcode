from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = ""
        # Compare character by character across all strings
        for i in range(len(strs[0])):
            char = strs[0][i]
            # Check if this character matches in all strings at position i
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != char:
                    return prefix
            prefix += char
        
        return prefix

sample = Solution()
print(sample.longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"


