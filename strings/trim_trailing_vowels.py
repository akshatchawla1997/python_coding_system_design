class StringPractice:

    def trimTrailingVowels(self, str):
        vowels = 'aeiou'
        return str.rstrip(vowels)
    
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            sol = haystack.find(needle)  
            return sol
        else:
            return -1
        
    
sol = StringPractice()
# z = sol.trimTrailingVowels("idaeiou")
z = sol.strStr('sadbutsad', 'sad')


print(z)

