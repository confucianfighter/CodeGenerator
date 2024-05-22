from PyQt5.QtWidgets import QWidget, QVBoxLayout, QScrollArea

from chat_bubble_pane import ChatBubblePane

class ChatThreadPane(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout()

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.chat_thread = QWidget()
        self.chat_thread_layout = QVBoxLayout()
        self.chat_thread.setLayout(self.chat_thread_layout)
        self.scroll_area.setWidget(self.chat_thread)

        self.layout.addWidget(self.scroll_area)
        self.setLayout(self.layout)

    def add_message_to_thread(self, sender, message):
        bubble = ChatBubblePane(sender, message, self)
        self.chat_thread_layout.addWidget(bubble)
        self.chat_thread_layout.addStretch(1)
        self.scroll_area.verticalScrollBar().setValue(self.scroll_area.verticalScrollBar().maximum())
