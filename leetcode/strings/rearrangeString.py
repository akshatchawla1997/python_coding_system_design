class Solution:
    def rearrangeString(self, s: str, x: str, y:str) -> str:
        count_x = s.count(x)
        count_y = s.count(y)
        if not(x in s and y in s):
            return s
        other = [char for char in s if char != x and char !=y]
        other_str = "".join(other)
        return count_y * y + other_str + count_x * x

        


s = Solution()
z = s.rearrangeString( s = "axe", x = "o", y = "x")
print(z)