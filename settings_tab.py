from PyQt5.QtWidgets import QWidget, QVBoxLayout, QScrollArea
from settings_pane import SettingsPane

class SettingsTab(QWidget):
    def __init__(self):
        super().__init__()
        
        self.layout = QVBoxLayout()
        
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        
        self.settings_pane = SettingsPane()
        self.scroll_area.setWidget(self.settings_pane)
        
        self.layout.addWidget(self.scroll_area)
        
        self.setLayout(self.layout)
