from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class ChatBubblePane(QWidget):
    def __init__(self, sender, message, parent=None):
        super().__init__(parent)
        
        self.layout = QVBoxLayout()
        
        self.bubble_label = QLabel(message)
        self.bubble_label.setWordWrap(True)
        self.bubble_label.setAlignment(Qt.AlignLeft if sender == "You" else Qt.AlignRight)
        
        if sender == "You":
            self.bubble_label.setStyleSheet("background-color: lightblue; padding: 10px; border-radius: 10px;")
        else:
            self.bubble_label.setStyleSheet("background-color: lightgreen; padding: 10px; border-radius: 10px;")
        
        self.layout.addWidget(self.bubble_label)
        self.setLayout(self.layout)
