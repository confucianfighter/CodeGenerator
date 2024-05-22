import json
import os

MAIN_SETTINGS_FILE = "settings.json"

def load_main_settings():
    if os.path.exists(MAIN_SETTINGS_FILE):
        with open(MAIN_SETTINGS_FILE, 'r') as file:
            settings = json.load(file)
    else:
        settings = {}
    return settings

def save_main_settings(settings):
    with open(MAIN_SETTINGS_FILE, 'w') as file:
        json.dump(settings, file, indent=4)

def add_main_setting(key, value):
    settings = load_main_settings()
    settings[key] = value
    save_main_settings(settings)

def retrieve_main_setting(key, default_value=None):
    settings = load_main_settings()
    return settings.get(key, default_value)

def get_project_settings_file(project_root):
    return os.path.join(project_root, "CodeGenerator", "project_settings.json")

def load_project_settings(project_root):
    settings_file = get_project_settings_file(project_root)
    if os.path.exists(settings_file):
        with open(settings_file, 'r') as file:
            settings = json.load(file)
    else:
        settings = {}
    return settings

def save_project_settings(project_root, settings):
    settings_dir = os.path.join(project_root, "CodeGenerator")
    if not os.path.exists(settings_dir):
        os.makedirs(settings_dir)
    settings_file = get_project_settings_file(project_root)
    with open(settings_file, 'w') as file:
        json.dump(settings, file, indent=4)

def add_project_setting(project_root, key, value):
    settings = load_project_settings(project_root)
    settings[key] = value
    save_project_settings(project_root, settings)

def retrieve_project_setting(project_root, key, default_value=None):
    settings = load_project_settings(project_root)
    return settings.get(key, default_value)
