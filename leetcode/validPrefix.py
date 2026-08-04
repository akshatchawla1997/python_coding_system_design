class Solution:
    def validPrefix(self, s: str) -> int :
        prefix, count0, count1 = 0, 0, 0
        for i in s:
            if i == '0':
                count0 += 1
            else:
                count1 += 1
            result = abs(count0 - count1)
            if result <= 1:
                prefix += 1
        return prefix

s = Solution()
print(s.validPrefix("00101"))  # Output: 