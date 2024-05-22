from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLabel
from settings_util import retrieve_project_setting, add_project_setting, retrieve_main_setting

class ProjectDescriptionPane(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent

        self.layout = QVBoxLayout()

        self.label = QLabel("Project Description:")
        self.description_box = QTextEdit()
        self.description_box.textChanged.connect(self.save_description)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.description_box)
        self.setLayout(self.layout)

        self.load_project_settings()

    def save_description(self):
        project_root = retrieve_main_setting("root_project_folder", "")
        if project_root:
            add_project_setting(project_root, "project_description", self.description_box.toPlainText())

    def load_project_settings(self):
        project_root = retrieve_main_setting("root_project_folder", "")
        description = retrieve_project_setting(project_root, "project_description", "")
        self.description_box.setText(description)
