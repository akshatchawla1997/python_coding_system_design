import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        
        print(math.gcd(self.sumFirstEvenNumbers(n), self.sumFistOddNumbers(n)))
    def sumFirstEvenNumbers(self, n):
        eSum = 0
        even =  list(range(2, (2*n)+1, 2))
        for i in even:
            eSum += i
        return eSum
    def sumFistOddNumbers(self, n):
        oSum = 0
        odd =  list(range(1, (2*n)+1, 2))
        for i in odd:
            oSum += i
        return oSum


s = Solution()  
s.gcdOfOddEvenSums(4)
 

