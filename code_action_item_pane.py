from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QVBoxLayout

class CodeActionItemPane(QWidget):
    def __init__(self, description, action_id, confirm_callback, deny_callback, parent=None):
        super().__init__(parent)
        self.action_id = action_id
        self.parent = parent
        self.confirm_callback = confirm_callback
        self.deny_callback = deny_callback

        self.layout = QHBoxLayout()

        self.action_label = QLabel(description)
        self.action_label.setWordWrap(True)
        self.action_label.setStyleSheet("background-color: lightyellow; padding: 10px; border-radius: 10px;")

        self.confirm_button = QPushButton("✔")
        self.confirm_button.setStyleSheet("background-color: green; color: white;")
        self.confirm_button.clicked.connect(self.confirm_action)

        self.deny_button = QPushButton("✖")
        self.deny_button.setStyleSheet("background-color: orange; color: white;")
        self.deny_button.clicked.connect(self.deny_action)

        self.layout.addWidget(self.action_label)
        self.layout.addWidget(self.confirm_button)
        self.layout.addWidget(self.deny_button)
        self.setLayout(self.layout)

    def confirm_action(self):
        self.confirm_callback(self.action_id)
        self.parent.remove_action(self)

    def deny_action(self):
        self.deny_callback(self.action_id)
        self.parent.remove_action(self)
