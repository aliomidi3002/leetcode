class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:

        tcell = n * n
        if tcell * w <= maxWeight:
            return tcell

        return maxWeight // w