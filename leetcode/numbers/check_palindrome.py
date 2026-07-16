class Solution:
    def checkPalindrome(self, num):
        q = num
        x = 0
        while(q > 0):
            r = q % 10
            q = q // 10
            x = (x * 10) + r
        print(x)
        if (x == num):
            return True
        else:
            return False
        
s = Solution()
print(s.checkPalindrome(1212))