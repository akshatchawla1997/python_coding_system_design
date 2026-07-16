class TextMemento:

    def __init__(self, text):
        self.__saved_text = text

    def get_saved_text(self):
        return self.__saved_text
    # bad example
#     def __init__(self):
#         self.__text = ""

#     def write(self, new_text):
#         self.__text += new_text

#     def get_text(self):
#         return self.__text
    

# textEditor = TextMemento()
# textEditor.write("hello")
# textEditor.write("World")
# textEditor.write("goodbye")
# print(textEditor.get_text())
# undo

# print(textEditor.get_text())