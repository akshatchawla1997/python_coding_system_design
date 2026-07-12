class CountVowelsInString:
    def __init__(self, input_string):
        self.input_string = input_string

    def count_vowels(self):
        count = 0
        for char in self.input_string:
            if char.lower() in 'aeiou':
                count += 1
        return count
    
input_string = input("Enter a string: ")
counter = CountVowelsInString(input_string)
print(counter.count_vowels())