class String:
    def __init__(self, string):
        self.string = string

    def reverse(self):
        return self.string[::-1]
    
    # def lengthOfLastWord(self) -> int:
    #     str = self.string.strip().split(" ")
    #     print(len(str[len(str)-1]))
           

s = String("Hello, World!")
print(s.reverse())  # Output: !dlroW ,olleH

s = String("   fly me   to   the moon  ")
print(s.reverse())  # Output: amanaP :lanac a ,nalp a ,nam A
# s.lengthOfLastWord()