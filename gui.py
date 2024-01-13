import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QScrollArea, QMessageBox, QTextEdit
from gmail_automation import sendEmail
from utils import emailFormatting

class App(QWidget):
    sender_email = ""
    subject = ""
    email_template = ""

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Mass Email Distribution")
        self.showMaximized()  # Maximize the window

        main_layout = QVBoxLayout(self)

        # Fields for sender email, subject
        self.sender_email_field = QLineEdit()
        self.sender_email_field.setPlaceholderText("Enter sender's email here...")
        main_layout.addWidget(self.sender_email_field)

        self.subject_field = QLineEdit()
        self.subject_field.setPlaceholderText("Enter email subject here...")
        main_layout.addWidget(self.subject_field)

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

        email_label = QLabel(f'Recipient Email {len(self.inputs) + 1}:')
        email_input = QLineEdit()
        name_label = QLabel('Recipient Name:')
        name_input = QLineEdit()  # Add a recipient name input field
        desc_label = QLabel('Description:')
        desc_input = QLineEdit()

        hbox.addWidget(email_label)
        hbox.addWidget(email_input)
        hbox.addWidget(name_label)
        hbox.addWidget(name_input)  # Add recipient name input field
        hbox.addWidget(desc_label)
        hbox.addWidget(desc_input)

        self.input_layout.addLayout(hbox)
        self.inputs.append((email_input, name_input, desc_input))

    def onSubmit(self):
        # Retrieve sender, subject
        self.sender_email = self.sender_email_field.text()
        self.subject = self.subject_field.text()

        print(self.sender_email, self.subject)
        # Process the inputs on submit
        self.email_template = self.template_field.toPlainText()
        print("Email Template:", self.email_template)  # Save the email template to a variable

        recipients = {}
        for email_input, name_input, desc_input in self.inputs:
            email = email_input.text()
            name = name_input.text()  # Retrieve recipient's name
            description = desc_input.text()
            if email:  # Store only if email is entered
                recipients[email] = {"name": name, "description": description}

        # Do something with the data (like storing it)
        print("data", recipients)  # For demonstration purposes

        # Show a message box
        QMessageBox.information(self, "DO NOT CLOSE THIS WINDOW UNTIL EMAILS HAVE BEEN SENT", "Please allow up to a few minutes for all of the emails to send!")

        i = 1
        items = len(recipients)

        for email, data in recipients.items():
            name = data["name"]
            description = data["description"]
            content = emailFormatting(description, self.email_template, name)
            print(content)

            sendEmail(self.sender_email, email, content, self.subject)
            
            #QMessageBox.information(self, f"Email {i}/{items} Sent", "The email has been sent!")

            i += 1

        QMessageBox.information(self, f"Email {i}/{items} has sent.", "You may now close this window")

def openApp():
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
