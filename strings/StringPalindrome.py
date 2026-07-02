import re
class StringPalindrome:
    def __init__(self, value):
        self.value = value

    def reverse(self):
        return self.value[::-1]
    
    def string_cleaner(self):
        # Remove non-alphanumeric characters and convert to lowercase
        cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', self.value).lower()
        print(cleaned_string)  # Debugging line to check the cleaned string
        return cleaned_string

str = 'A man, a plan, a canal: Panama' # A man, a plan, a canal: Panama Output: amanaP :lanac a ,nalp a ,nam A 
s = StringPalindrome(str)
if s.string_cleaner() == s.string_cleaner()[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")