from math import *
class Solution:
    def checkArmstrong(self, num):
        q = num
        x = 0
        armstrong = 0
        count = int(log10(num) + 1)
        while(q > 0):
            r = q % 10
            q = q // 10
            x = (x * 10) + r
            armstrong = (r ** count) + armstrong
        print(armstrong)
        if (armstrong == num):
            return True
        else:
            return False
        
s = Solution()
print(s.checkArmstrong(153))