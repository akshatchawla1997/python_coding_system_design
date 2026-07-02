class String:
    def __init__(self, string):
        self.string = string

    def reverse(self):
        return self.string[::-1]

s = String("Hello, World!")
print(s.reverse())  # Output: !dlroW ,olleH

s = String("Akshat")
print(s.reverse())  # Output: tahxkA