# validate user input for a string
# 1. Username is not more than 12 characters
# 2. Username should not contain spaces
# 3. Username should not contain digits

class StringValidator:
    def __init__(self, username):
        self.username = username
    
    def is_valid(self):
        if len(self.username) <= 12 and self.username != "" and self.username.isalpha():
            return True
        else:
            return False

input_username = input("Enter a username: ")
validator = StringValidator(input_username)
x = validator.is_valid()
print(x)