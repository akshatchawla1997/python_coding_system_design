from math import *
class Solution:
    def primeFactors(self, num):
        check = True
        factors = [1, num]
        # while(check):
        for i in range(2, int(sqrt(num))+1):
            if (num % i == 0):
                if(num//i != i):
                    factors.append(i)
                    factors.append(num//i)

            #     check = False
            # else:
        return (factors)
s = Solution()
print(s.primeFactors(25))