import sys
class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        end_list = [int(x) for x in endTime.split(':')]
        endSeconds = (end_list[0]*3600) + (end_list[1] * 60) + (end_list[2])
        start_list = [int(x) for x in startTime.split(':')]
        startSeconds = (start_list[0]*3600) + (start_list[1] * 60) + (start_list[2])
        return  endSeconds - startSeconds



s = Solution()

ex1 = s.secondsBetweenTimes(startTime = "01:00:00", endTime = "01:00:25")
ex2 = s.secondsBetweenTimes(startTime = "12:34:56", endTime = "13:00:00")

print(ex1, ex2)