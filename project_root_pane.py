from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QMessageBox
from settings_util import add_main_setting, retrieve_main_setting, save_main_settings, load_main_settings
import os

class ProjectRootPane(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent

        self.layout = QVBoxLayout()

        # Create a vertical layout for the file picker
        self.file_picker_layout = QVBoxLayout()
        self.file_path_label = QLabel()
        self.file_picker_button = QPushButton("Change")
        self.file_picker_button.clicked.connect(self.open_file_picker)
        self.file_picker_layout.addWidget(self.file_path_label)
        self.file_picker_layout.addWidget(self.file_picker_button)

        self.layout.addLayout(self.file_picker_layout)
        self.layout.addStretch(1)
        self.setLayout(self.layout)

        self.update_file_path_label()

    def open_file_picker(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Root Project Folder")
        if folder:
            self.check_and_create_project_folder(folder)
            add_main_setting("root_project_folder", folder)
            self.update_file_path_label()
            print(f"Selected folder: {folder}")

    def check_and_create_project_folder(self, folder):
        code_generator_path = os.path.join(folder, "CodeGenerator")
        if not os.path.exists(code_generator_path):
            reply = QMessageBox.question(self, "Create Folder",
                                         f"The folder 'CodeGenerator' does not exist in {folder}. Would you like to create it?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                os.makedirs(code_generator_path)
                QMessageBox.information(self, "Folder Created",
                                        f"The folder 'CodeGenerator' has been created in {folder}.")
                save_main_settings(load_main_settings())
            else:
                QMessageBox.warning(self, "Folder Not Created",
                                    "The 'CodeGenerator' folder was not created. Please select another folder or create the folder manually.")

    def update_file_path_label(self):
        folder = retrieve_main_setting("root_project_folder", "")
        self.file_path_label.setText(folder)
