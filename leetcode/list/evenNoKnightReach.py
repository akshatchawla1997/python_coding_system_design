class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        startSum = start[0] + start[1]
        targetSum = target[0] + target[1]

        return (startSum % 2 == targetSum % 2)
    
s = Solution()
print(s.canReach(start = [4,5], target = [6,6]))