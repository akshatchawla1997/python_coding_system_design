class StringPalindrome:
    def __init__(self, value):
        self.value = value

    def reverse(self):
        return self.value[::-1]
str = input("Enter a string: ")
s = StringPalindrome(str)
if s.reverse() == str:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")