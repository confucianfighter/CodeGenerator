import os

class CRUDOperations:
    ZWSP = '\u200B'  # Zero Width Space character

    def __init__(self, base_path):
        self.base_path = base_path

    def add_folder(self, folder_name):
        folder_path = os.path.join(self.base_path, folder_name)
        try:
            os.makedirs(folder_path)
            print(f"Folder '{folder_path}' created successfully.")
        except FileExistsError:
            print(f"Folder '{folder_path}' already exists.")
        except Exception as e:
            print(f"Error creating folder '{folder_path}': {e}")

    def remove_folder(self, folder_name):
        folder_path = os.path.join(self.base_path, folder_name)
        try:
            os.rmdir(folder_path)
            print(f"Folder '{folder_path}' removed successfully.")
        except FileNotFoundError:
            print(f"Folder '{folder_path}' not found.")
        except Exception as e:
            print(f"Error removing folder '{folder_path}': {e}")

    def add_file(self, file_name):
        file_path = os.path.join(self.base_path, file_name)
        try:
            with open(file_path, 'w') as file:
                pass
            print(f"File '{file_path}' created successfully.")
        except Exception as e:
            print(f"Error creating file '{file_path}': {e}")

    def remove_file(self, file_name):
        file_path = os.path.join(self.base_path, file_name)
        try:
            os.remove(file_path)
            print(f"File '{file_path}' removed successfully.")
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        except Exception as e:
            print(f"Error removing file '{file_path}': {e}")

    def insert_at_line(self, file_name, line_number, content):
        file_path = os.path.join(self.base_path, file_name)
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()

            lines.insert(line_number, content + '\n')

            with open(file_path, 'w') as file:
                file.writelines(lines)
            print(f"Inserted content at line {line_number} in file '{file_path}'.")
        except Exception as e:
            print(f"Error inserting content at line {line_number} in file '{file_path}': {e}")

    def remove_lines(self, file_name, start_line, end_line):
        file_path = os.path.join(self.base_path, file_name)
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()

            del lines[start_line:end_line+1]

            with open(file_path, 'w') as file:
                file.writelines(lines)
            print(f"Removed lines {start_line} to {end_line} from file '{file_path}'.")
        except Exception as e:
            print(f"Error removing lines {start_line} to {end_line} from file '{file_path}': {e}")

    

    

# Testing the new methods
def test_invisible_lines():
    base_path = 'test_env'
    if not os.path.exists(base_path):
        os.makedirs(base_path)

    crud = CRUDOperations(base_path)
    file_name = 'test_file.txt'
    
    crud.add_file(file_name)
    crud.insert_at_line(file_name, 0, 'Visible line 1')
    crud.insert_at_line(file_name, 1, 'Visible line 2')
    crud.insert_at_line(file_name, 2, 'Visible line 3')

    # Mark the second line as invisible
    crud.mark_line_invisible(file_name, 1)

    # Read the file ignoring invisible lines
    visible_lines = crud.read_file_ignoring_invisible_lines(file_name)
    print("Visible lines:")
    for line in visible_lines:
        print(line.strip())

if __name__ == "__main__":
    test_invisible_lines()
