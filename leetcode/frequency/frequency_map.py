class Solution:
    def frequency_mapM1(self, nums):# tc = O(n), SC = O(N)
        frequencyDict = {}
        for i in nums:
            if i in frequencyDict:
                frequencyDict[i] += 1
            else:
                frequencyDict[i] = 1
        print(frequencyDict)
# using get method as normally if you try to look up a key that dosen't exist in a dictionary, python crashes
# with a keyError. the .get() method prevents this by letting you provide a backup plan(a default value)
# syntax = dictionary.get(key, default_value)
    def frequency_MapM2(self, nums): # # tc = O(n), SC = O(1)
        hashMap = {}
        for i in nums:
            hashMap[i] = hashMap.get(i, 0) + 1
        print(f"hash map {hashMap}")

s = Solution()
s.frequency_mapM1([5, 6, 7, 7, 1, 9, 111, 1, 1, 5, 1, 1])
s.frequency_MapM2([5, 6, 7, 7, 1, 9, 111, 1, 1, 5, 1, 1])