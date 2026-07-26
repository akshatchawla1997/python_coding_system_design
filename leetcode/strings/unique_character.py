# First Unique Character in a String

class Solution:
    def uniqueCharacter(self, s:str)->int:
        hash_map = {}
        for i in s:
            hash_map[i] = hash_map.get(i, 0) + 1
        
        for index, char in enumerate(s):
            if hash_map[char] == 1:
                return index
        
        return -1



s= Solution()
print(s.uniqueCharacter("loveleetcode"))