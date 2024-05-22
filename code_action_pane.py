from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea

from code_action_item_pane import CodeActionItemPane

class CodeActionPane(QWidget):
    def __init__(self, confirm_callback, deny_callback, parent=None):
        super().__init__(parent)
        self.confirm_callback = confirm_callback
        self.deny_callback = deny_callback

        self.layout = QVBoxLayout()

        self.label = QLabel("Action Required")
        self.layout.addWidget(self.label)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.actions_widget = QWidget()
        self.actions_layout = QVBoxLayout()
        self.actions_widget.setLayout(self.actions_layout)
        self.scroll_area.setWidget(self.actions_widget)

        self.layout.addWidget(self.scroll_area)
        self.setLayout(self.layout)

        self.populate_actions()

    def populate_actions(self):
        for i in range(20):
            description = f"Do you want to execute action {i+1}?"
            self.add_code_action(description, i+1)

    def add_code_action(self, description, action_id):
        action_item = CodeActionItemPane(description, action_id, self.confirm_callback, self.deny_callback, self)
        self.actions_layout.addWidget(action_item)

    def remove_action(self, action_item):
        self.actions_layout.removeWidget(action_item)
        action_item.deleteLater()
