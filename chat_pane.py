from PyQt5.QtWidgets import QWidget, QVBoxLayout

from chat_thread_pane import ChatThreadPane
from message_input_pane import MessageInputPane
from code_action_pane import CodeActionPane

class ChatPane(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.chat_thread_pane = ChatThreadPane(self)
        self.message_input_pane = MessageInputPane(self)
        self.code_action_pane = CodeActionPane(self.confirm_action, self.deny_action, self)

        self.layout.addWidget(self.chat_thread_pane)
        self.layout.addWidget(self.message_input_pane)
        self.layout.addWidget(self.code_action_pane)
        self.setLayout(self.layout)

    def add_message_to_thread(self, sender, message):
        self.chat_thread_pane.add_message_to_thread(sender, message)

    def confirm_action(self, action_id):
        print(f"Action {action_id} confirmed.")
        # Add code to handle the confirmation of the action

    def deny_action(self, action_id):
        print(f"Action {action_id} denied.")
        # Add code to handle the denial of the action
