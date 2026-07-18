from math import *
class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        sequence = [0] * n
        sequence[0] = s
        print(sequence)
        for i in range(0, n):
            less_pair = abs(sequence[i] - sequence[i-1])  
            more_pair = abs(sequence[i] - sequence[i-1] )
            print(less_pair, more_pair)



s = Solution()

print(s.maximumValue( n = 4, s = 3, m = 5))

# adjacent pair= seq[i] - seq[i-1] <= m