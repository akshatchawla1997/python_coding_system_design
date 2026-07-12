# Ransom Note
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # return not (Counter(ransomNote) - Counter(magazine))
        for i in ransomNote:
            if i not in magazine:
                return False
        return True


s = Solution()
z = s.canConstruct("aa", "aab")
print(z)