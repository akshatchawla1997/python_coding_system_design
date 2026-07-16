from math import *
class Solution:
    def extractionOfDigits(self, num):
        q = num
        # count = 0
        while(q > 0):
            r = q % 10
            q = q//10
        #     count = count + 1
        # return count
    def countnoOfDigits(self, num):
        return int(log10(num) + 1)
    
    
    
        
s = Solution()
print(s.extractionOfDigits(5873))
print(s.countnoOfDigits(586374))
# time complexity of this code will be O(log10) because division is taken place and whenever we divide a number with some digit or another number then the complexity becomes base of that number