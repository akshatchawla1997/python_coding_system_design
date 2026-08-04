from typing import List
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        results = set()
        if all(d % 2 == 1 for d in digits):
            return []
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i == j or j == k or i == k:
                        continue
                    a, b, c = digits[i], digits[j], digits[k]
                    if a == 0:
                        continue
                    num = a* 100 + b*10 + c
                    if num % 2 == 0:
                        results.add(num)
        return sorted(list(results))

s = Solution()
print(s.findEvenNumbers([2, 1, 3, 0]))  #
    