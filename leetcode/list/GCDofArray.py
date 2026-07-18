from math import *
from typing import List

class Solution:
    # def findGCD(self, nums: List[int]) -> int:
    #     return gcd(min(nums), max(nums))

    def calculateGCD(self, min, max):
        gcd = 1
        for i in range(2, min+1):
            if (min % i == 0 and max % i == 0):
                gcd = i
        return gcd


    def findGCD(self, nums: List[int]) -> int:
        min = nums[0]
        max = nums[0]
        for i in nums:
            if i < min:
                min = i
            else:
                max = i
        return self.calculateGCD(min, max)
        

s = Solution()
# nums = [2,5,6,9,10]
# nums = [7,5,6,8,3]
nums = [3,3]
print(s.findGCD(nums))