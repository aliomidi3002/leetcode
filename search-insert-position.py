class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if target > nums[-1]:
            return len(nums)

        diff = 0
        for i in range(len(nums)):
            if target - nums[i] > 0:
                diff = target - nums[i]
            elif diff == 0:
                return i
            else:
                return i