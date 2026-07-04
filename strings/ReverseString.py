class String:
    def __init__(self, string):
        self.string = string

    def reverse(self):
        return self.string[::-1]
    
    def lengthOfLastWord(self) -> int:
        str = self.string.strip().split(" ")
        print(len(str[len(str)-1]))
        # i = str[len(str)-1]
        # count = 0 
        # for i in self.string[::-1]:
        #     if(i != " "):
        #         count = (len(str[len(str)-1]))
        #         print(f"count is {count}")  
        # return count
        
            

# s = String("Hello, World!")
# print(s.reverse())  # Output: !dlroW ,olleH

s = String("   fly me   to   the moon  ")
print(s.reverse())  # Output: amanaP :lanac a ,nalp a ,nam A
s.lengthOfLastWord()