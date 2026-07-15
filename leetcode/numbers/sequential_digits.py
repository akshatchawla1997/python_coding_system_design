from typing import List

class Solution:
    def check_sequencial_digit(self, num)->bool:
        strNum = str(num)
        return str(num) in strNum


    def sequentialDigits(self, low: int, high: int) -> List[int]:
        results = []
        for i in range(low, high):
            if(self.check_sequencial_digit(i)):
                results.append(i)
        return results




s = Solution()
z = s.sequentialDigits(low = 10, high = 1000000000)
print(z)