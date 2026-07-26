# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# return true if the occurence of character is same in both string otherwise return false

from collections import defaultdict


class ValidAnagram:
    def __init__(self, s, t):
        self.s = s
        self.t = t

    def is_anagram(self):
        if len(self.s) != len(self.t):
            return False
        count_s = defaultdict(int)
        count_t = defaultdict(int)
        print(count_s)
        print(count_t)

        for char_s, char_t in zip(self.s, self.t):
            count_s[char_s] += 1
            count_t[char_t] += 1

        if count_s == count_t:
            return True
        else:
            return False

va = ValidAnagram("anagram", "nagaram")
print(va.is_anagram())