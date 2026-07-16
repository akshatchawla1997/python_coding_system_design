from design_patterns.behavioral_design_pattern.memento_pattern.history import History
from design_patterns.behavioral_design_pattern.memento_pattern.text_editor import TextEditor
from design_patterns.behavioral_design_pattern.memento_pattern.text_Memento import TextMemento

textEditor = TextEditor()
history = History()

textEditor.write("hello")
textEditor.write(" world")

history.save_state(textEditor.save())
textEditor.write(" Good")
textEditor.write(" bye")
history.save_state(textEditor.save())
history.get_history()
print("-----------------")
textEditor.restore(history.undo())
print(textEditor.get_text())
