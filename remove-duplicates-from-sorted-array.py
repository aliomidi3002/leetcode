class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        idx = 0
        flg = -999
        count = 0
        for i in nums:
            if i != flg:
                flg = i
                nums[idx] = flg
                idx += 1
        
        return idx