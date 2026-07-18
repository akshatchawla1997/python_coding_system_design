from math import *
from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            nums.append(nums[i])
        return nums



s = Solution()
nums = [1, 3 ,  2, 1]
print(s.getConcatenation(nums))

# adjacent pair= seq[i] - seq[i-1] <= m