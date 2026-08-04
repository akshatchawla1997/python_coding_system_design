class Solution:
    def palindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] !=s[right]:
                return False
            left += 1
            right -= 1
        return True

    def is_palindrome(self, s: str, left=0, right=None) -> bool:
        if right is None:
            right = len(s) - 1
        if left >= right:
            return True
        if s[left] != s[right]:
            return False
        return self.is_palindrome(s, left + 1, right - 1)