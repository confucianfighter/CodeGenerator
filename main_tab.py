from PyQt5.QtWidgets import QWidget, QVBoxLayout
from chat_pane import ChatPane

class MainTab(QWidget):
    def __init__(self):
        super().__init__()
        
        self.layout = QVBoxLayout()
        
        self.chat_pane = ChatPane()
        
        self.layout.addWidget(self.chat_pane)
        
        self.setLayout(self.layout)
