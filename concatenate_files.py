import os
import sys

def concatenate_files(folder_path):
    output_text = []
    separator = "\n" + "-" * 50 + "\n"
    
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    file_content = f.read()
                    output_text.append(separator)
                    output_text.append(f"{file_path}\n{separator}")
                    output_text.append(file_content)
    
    return "".join(output_text)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python concatenate_files.py <folder_path>")
        sys.exit(1)
    
    folder_path = sys.argv[1]
    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid directory.")
        sys.exit(1)
    
    concatenated_text = concatenate_files(folder_path)
    output_file = "concatenated_output.txt"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(concatenated_text)
    
    print(f"All .py files have been concatenated into {output_file}")
