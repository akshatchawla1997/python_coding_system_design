class Solution:
    def primeFactors(self, num):
        check = True
        factors = [1, num]
        # while(check):
        for i in range(2, num//2 + 1):
            if not (num % i == 0):
                check = False
            else:
                factors.append(i)
        return (factors)
s = Solution()
print(s.primeFactors(20))