class String:
    def __init__(self, string):
        self.string = string

    def reverse(self):
        return self.string[::-1]

# s = String("Hello, World!")
# print(s.reverse())  # Output: !dlroW ,olleH

s = String("A man, a plan, a canal: Panama")
print(s.reverse())  # Output: amanaP :lanac a ,nalp a ,nam A