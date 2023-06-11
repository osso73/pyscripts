from PySide6.QtWidgets import QTextEdit, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton

class FindReplace(QDialog):
    def __init__(self, text_edit):
        super().__init__()

        self.text_edit = text_edit
        # Create a dialog window for the "Find and Replace" operation
        self.setWindowTitle("Find and Replace")

        # Create a layout for the dialog window
        layout = QVBoxLayout(self)

        # Add a label and a line edit widget for the "Find" operation
        find_label = QLabel("Find:")
        self.find_line_edit = QLineEdit()
        layout.addWidget(find_label)
        layout.addWidget(self.find_line_edit)

        # Add a label and a line edit widget for the "Replace" operation
        replace_label = QLabel("Replace:")
        self.replace_line_edit = QLineEdit()
        layout.addWidget(replace_label)
        layout.addWidget(self.replace_line_edit)

        # Add a "Find and Replace" button
        find_replace_button = QPushButton("Find and Replace ALL")
        layout.addWidget(find_replace_button)

        find_replace_button.clicked.connect(self.find_and_replace)

        # Show the dialog window
        self.exec_()
        

    # Connect the "Find and Replace" button to a function that performs the operation
    def find_and_replace(self):
        # Get the text to find and replace
        find_text = self.find_line_edit.text()
        replace_text = self.replace_line_edit.text()

        # Get the current cursor position in the text edit
        cursor = self.text_edit.textCursor()
        cursor_pos = cursor.position()

        # Search for the text to replace
        text = self.text_edit.toPlainText()
        new_text = text.replace(find_text, replace_text)

        # Update the text in the text edit
        self.text_edit.setPlainText(new_text)

        # Move the cursor to the position where the text was found
        new_cursor = self.text_edit.textCursor()
        new_cursor.setPosition(cursor_pos)
        self.text_edit.setTextCursor(new_cursor)

        # Close the dialog window
        self.close()