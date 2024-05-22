import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget
from settings_tab import SettingsTab
from main_tab import MainTab
from github_tab import GitHubTab

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Tabbed Interface")
        self.setGeometry(100, 100, 800, 600)

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.settings_tab = SettingsTab()
        self.tabs.addTab(self.settings_tab, "Settings")
        self.main_tab = MainTab()
        self.tabs.addTab(self.main_tab, "Main")
        self.github_tab = GitHubTab()
        self.tabs.addTab(self.github_tab, "GitHub")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
