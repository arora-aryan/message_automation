#Copyright MicroLearn, Aryan Arora

#This program takes in a csv file

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QScrollArea, QMessageBox, QTextEdit

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Dynamic Email and Description Collector")
        self.showMaximized()  # Maximize the window

        main_layout = QVBoxLayout(self)

        # Large text field for email template
        self.template_field = QTextEdit()
        self.template_field.setPlaceholderText("Enter email template here...")
        main_layout.addWidget(self.template_field)

        # Scrollable area for the input fields
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        scroll_widget = QWidget()
        self.scroll_area.setWidget(scroll_widget)
        self.input_layout = QVBoxLayout(scroll_widget)
        main_layout.addWidget(self.scroll_area)

        self.inputs = []
        self.addField()

        # Layout for buttons at the bottom
        buttons_layout = QHBoxLayout()
        self.add_button = QPushButton('Add More', self)
        self.add_button.clicked.connect(self.addField)
        buttons_layout.addWidget(self.add_button)

        submit_button = QPushButton('Submit', self)
        submit_button.clicked.connect(self.onSubmit)
        buttons_layout.addWidget(submit_button)

        # Add buttons layout to the main layout
        main_layout.addLayout(buttons_layout)

    def addField(self):
        if len(self.inputs) >= 30:
            self.add_button.setDisabled(True)
            return

        hbox = QHBoxLayout()

        email_label = QLabel(f'Email {len(self.inputs) + 1}:')
        email_input = QLineEdit()
        desc_label = QLabel('Description:')
        desc_input = QLineEdit()

        hbox.addWidget(email_label)
        hbox.addWidget(email_input)
        hbox.addWidget(desc_label)
        hbox.addWidget(desc_input)

        self.input_layout.addLayout(hbox)
        self.inputs.append((email_input, desc_input))

    def onSubmit(self):
        # Process the inputs on submit
        email_template = self.template_field.toPlainText()
        print("Email Template:", email_template)  # Save the email template to a variable

        data = {}
        for email_input, desc_input in self.inputs:
            email = email_input.text()
            description = desc_input.text()
            if email:  # Store only if email is entered
                data[email] = description

        # Do something with the data (like storing it)
        print(data)  # For demonstration purposes

        # Show a message box
        QMessageBox.information(self, "Submission Status", "You may now close this window. Please allow up to a few minutes for all of the emails to send!")

def main():
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()