class Solution:
    def plusOne(self, num):
        digitList = [int(x) for x in str(num)]
        digitList[len(digitList)-1] += 1
        n = 0
        for digit in digitList:
            n = (n * 10) + digit
        return n
    

s = Solution()
print(s.plusOne(1234))