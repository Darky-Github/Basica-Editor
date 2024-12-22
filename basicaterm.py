import os

class BasicaTerm:
    def __init__(self):
        self.file_path = None
        self.text_lines = []

    def display_menu(self):
        print("\nBasicaTerm - Terminal-Based Text Editor")
        print("1. New File")
        print("2. Open File")
        print("3. Save File")
        print("4. Save As")
        print("5. View File")
        print("6. Find Text")
        print("7. Quit")
        choice = input("Select an option: ")
        return choice

    def new_file(self):
        self.file_path = None
        self.text_lines = []
        print("New file created. You can start typing your text below:")
        self.text_lines = self.get_text_input()

    def open_file(self):
        self.file_path = input("Enter the file path to open: ")
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                self.text_lines = file.readlines()
            print(f"File '{self.file_path}' opened successfully.")
        else:
            print("File not found.")

    def save_file(self):
        if self.file_path:
            with open(self.file_path, 'w') as file:
                file.writelines(self.text_lines)
            print(f"File '{self.file_path}' saved successfully.")
        else:
            self.save_as_file()

    def save_as_file(self):
        self.file_path = input("Enter the new file path to save: ")
        with open(self.file_path, 'w') as file:
            file.writelines(self.text_lines)
        print(f"File '{self.file_path}' saved successfully.")

    def view_file(self):
        print("\n".join(self.text_lines))

    def find_text(self):
        search_text = input("Enter text to find: ")
        found = False
        for line_num, line in enumerate(self.text_lines, start=1):
            if search_text in line:
                print(f"Found '{search_text}' in line {line_num}: {line.strip()}")
                found = True
        if not found:
            print(f"'{search_text}' not found.")

    def get_text_input(self):
        print("Enter text (type 'END' on a new line to finish):")
        text_lines = []
        while True:
            line = input()
            if line.upper() == 'END':
                break
            text_lines.append(line + '\n')
        return text_lines

    def run(self):
        while True:
            choice = self.display_menu()
            if choice == '1':
                self.new_file()
            elif choice == '2':
                self.open_file()
            elif choice == '3':
                self.save_file()
            elif choice == '4':
                self.save_as_file()
            elif choice == '5':
                self.view_file()
            elif choice == '6':
                self.find_text()
            elif choice == '7':
                print("Exiting BasicaTerm.")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    editor = BasicaTerm()
    editor.run()
