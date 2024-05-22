from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton
from PyQt5.QtCore import Qt, QEvent

class MessageInputPane(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout()

        self.input_box = QTextEdit()
        self.input_box.setPlaceholderText("Type your message here...")
        self.input_box.setFixedHeight(100)
        self.input_box.installEventFilter(self)

        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)

        self.layout.addWidget(self.input_box)
        self.layout.addWidget(self.send_button)
        self.setLayout(self.layout)

    def eventFilter(self, obj, event):
        if obj == self.input_box and event.type() == QEvent.KeyPress and event.key() == Qt.Key_Return and event.modifiers() == Qt.ShiftModifier:
            self.send_message()
            return True
        return super().eventFilter(obj, event)

    def send_message(self):
        message = self.input_box.toPlainText().strip()
        if message:
            self.parent().add_message_to_thread("You", message)
            self.input_box.clear()
            # Here you would normally send the message to the backend or API
            # For now, we'll just echo the message back
            self.parent().add_message_to_thread("Bot", message)
