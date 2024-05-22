from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox
from github import Github
import os
import subprocess
from settings_util import add_main_setting, retrieve_main_setting, add_project_setting, retrieve_project_setting
import re

class GitHubTab(QWidget):
    def __init__(self):
        super().__init__()
        root_project_folder = retrieve_main_setting("root_project_folder", "")
        self.layout = QVBoxLayout()

        # GitHub Access Token
        self.token_label = QLabel("GitHub Access Token:")
        self.token_input = QLineEdit()
        self.token_input.setText(retrieve_main_setting('github_token', ''))
        self.layout.addWidget(self.token_label)
        self.layout.addWidget(self.token_input)

        # GitHub Username
        self.username_label = QLabel("GitHub Username:")
        self.username_input = QLineEdit()
        self.username_input.setText(retrieve_main_setting('github_username', ''))
        self.layout.addWidget(self.username_label)
        self.layout.addWidget(self.username_input)

        # Repository Name
        self.repo_name_label = QLabel("Repository Name:")
        self.repo_name_input = QLineEdit()
        self.repo_name_input.setText(retrieve_project_setting(root_project_folder, 'github_repo_name', ''))
        self.layout.addWidget(self.repo_name_label)
        self.layout.addWidget(self.repo_name_input)

        # Repository Description
        self.repo_desc_label = QLabel("Repository Description:")
        self.repo_desc_input = QTextEdit()
        self.repo_desc_input.setPlainText(retrieve_project_setting(root_project_folder, 'github_repo_desc', ''))
        self.layout.addWidget(self.repo_desc_label)
        self.layout.addWidget(self.repo_desc_input)

        # Commit Message
        self.commit_message_label = QLabel("Commit Message:")
        self.commit_message_input = QLineEdit()
        self.commit_message_input.setText(retrieve_project_setting(root_project_folder, 'github_commit_message', ''))
        self.layout.addWidget(self.commit_message_label)
        self.layout.addWidget(self.commit_message_input)

        # Create Repo Button
        self.create_repo_button = QPushButton("Create Repository")
        self.create_repo_button.clicked.connect(self.create_repo)
        self.layout.addWidget(self.create_repo_button)

        # Push Changes Button
        self.push_button = QPushButton("Push Changes")
        self.push_button.clicked.connect(self.push_changes)
        self.layout.addWidget(self.push_button)

        # Rewind Button
        self.rewind_button = QPushButton("Rewind Changes")
        self.rewind_button.clicked.connect(self.rewind_changes)
        self.layout.addWidget(self.rewind_button)

        self.setLayout(self.layout)

    def sanitize_description(self, description):
        # Remove all control characters and keep only printable ones
        return re.sub(r'[\x00-\x1F\x7F]', '', description)

    def validate_path(self, path):
        # Check for valid Windows path
        if not os.path.isabs(path):
            return False
        try:
            os.listdir(path)
            return True
        except (OSError, IOError):
            return False

    def create_repo(self):
        token = self.token_input.text()
        username = self.username_input.text()
        repo_name = self.repo_name_input.text()
        repo_desc = self.repo_desc_input.toPlainText()
        root_project_folder = retrieve_main_setting("root_project_folder", "")
        print("Project root is" + root_project_folder)
        if not self.validate_path(root_project_folder):
            QMessageBox.critical(self, "Error", "Invalid project root directory." + root_project_folder)
            return

        # Save main settings
        add_main_setting('github_token', token)
        add_main_setting('github_username', username)

        # Save project settings
        add_project_setting(root_project_folder, 'github_repo_name', repo_name)
        add_project_setting(root_project_folder, 'github_repo_desc', repo_desc)

        repo_desc = self.sanitize_description(repo_desc)  # Sanitize the description

        g = Github(token)
        user = g.get_user()

        try:
            repo = user.create_repo(
                name=repo_name,
                description=repo_desc,
                private=False  # Change to True if you want to create a private repository
            )
            # Initialize the repo with a README file
            repo.create_file("README.md", "Initial commit", f"# {repo_name}\n\n{repo_desc}")
            QMessageBox.information(self, "Success", f"Repository '{repo_name}' created successfully.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error creating repository: {e}")

        # Initialize local repository
        self.initialize_local_repo(repo_name, root_project_folder)

    def initialize_local_repo(self, repo_name, root_project_folder):
        try:
            
            ### Run these commands: echo "# CodeGenerator" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/confucianfighter/CodeGenerator.git
# git push -u origin main

            os.chdir(root_project_folder)
            with open('README.md', 'w') as f:
                f.write(f"# {repo_name}\n\n")
            subprocess.run(['git', 'init'], check=True)
            # add .gitignore with .env and settings.json as well as __cache__ and __pycache__
            # create .gitignore file
            #subprocess.run(['echo', '.env\nsettings.json\n__cache__\n__pycache__', '>>', '.gitignore'], check=True)
            with open('.gitignore', 'w') as f:
                f.write('.env\nsettings.json\n__cache__\n__pycache__\n')
            subprocess.run(['git', 'add', '.'], check=True)
            subprocess.run(['git', 'commit', '-m', 'first commit'], check=True)
            subprocess.run(['git', 'branch', '-M', 'main'], check=True)
            subprocess.run(['git', 'push', '-u', 'origin', 'main'], check=True)
            
            QMessageBox.information(self, "Success", "Local repository initialized and pushed to GitHub.")
        except subprocess.CalledProcessError as e:
            QMessageBox.critical(self, "Error", f"Error initializing local repository: {e}")

    def push_changes(self):
        commit_message = self.commit_message_input.text()

        token = self.token_input.text()
        username = self.username_input.text()
        repo_name = self.repo_name_input.text()
        root_project_folder = retrieve_main_setting("root_project_folder", "")

        if not self.validate_path(root_project_folder):
            QMessageBox.critical(self, "Error", "Invalid project root directory.")
            return

        g = Github(token)
        user = g.get_user()
        repo = user.get_repo(repo_name)

        try:
            os.chdir(root_project_folder)  # Change directory to project root
            subprocess.run(['git', 'add', '.'], check=True)
            subprocess.run(['git', 'commit', '-m', commit_message], check=True)
            subprocess.run(['git', 'push'], check=True)
            QMessageBox.information(self, "Success", "Changes pushed to GitHub.")
        except subprocess.CalledProcessError as e:
            QMessageBox.critical(self, "Error", f"Error pushing changes: {e}")

    def rewind_changes(self):
        token = self.token_input.text()
        repo_name = self.repo_name_input.text()
        root_project_folder = retrieve_main_setting("root_project_folder", "")

        if not self.validate_path(root_project_folder):
            QMessageBox.critical(self, "Error", "Invalid project root directory.")
            return

        g = Github(token)
        user = g.get_user()
        repo = user.get_repo(repo_name)

        try:
            commits = repo.get_commits()
            if commits.totalCount > 1:
                last_commit_sha = commits[1].sha
                os.chdir(root_project_folder)  # Change directory to project root
                subprocess.run(['git', 'reset', '--hard', last_commit_sha], check=True)
                subprocess.run(['git', 'push', '--force'], check=True)
                QMessageBox.information(self, "Success", "Rewind to the previous commit successful.")
            else:
                QMessageBox.warning(self, "Warning", "No previous commit to rewind to.")
        except subprocess.CalledProcessError as e:
            QMessageBox.critical(self, "Error", f"Error rewinding changes: {e}")
