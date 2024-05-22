from PyQt5.QtWidgets import QWidget, QVBoxLayout

from project_root_pane import ProjectRootPane
from project_description_pane import ProjectDescriptionPane

class SettingsPane(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.project_root_pane = ProjectRootPane(self)
        self.project_description_pane = ProjectDescriptionPane(self)

        self.layout.addWidget(self.project_root_pane)
        self.layout.addWidget(self.project_description_pane)

        self.setLayout(self.layout)

        self.project_root_pane.update_file_path_label()
        self.project_description_pane.load_project_settings()
