import tkinter as tk
from tkinter import filedialog, messagebox

class BasicaEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Basica Editor")

        self.text_area = tk.Text(root, wrap='word', undo=True)
        self.text_area.pack(fill='both', expand=True)

        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Find", command=self.find_text)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)

        self.theme_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.theme_menu.add_command(label="Light Mode", command=lambda: self.change_theme('light'))
        self.theme_menu.add_command(label="Dark Mode", command=lambda: self.change_theme('dark'))
        self.menu_bar.add_cascade(label="Theme", menu=self.theme_menu)

        self.file_path = None

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.file_path = None
        self.root.title("Basica Editor - New File")

    def open_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if self.file_path:
            with open(self.file_path, 'r') as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())
            self.root.title(f"Basica Editor - {self.file_path}")

    def save_file(self):
        if self.file_path:
            with open(self.file_path, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))
        else:
            self.save_as_file()

    def save_as_file(self):
        self.file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                      filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if self.file_path:
            with open(self.file_path, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.root.title(f"Basica Editor - {self.file_path}")

    def find_text(self):
        find_popup = tk.Toplevel(self.root)
        find_popup.title("Find")
        find_popup.geometry("300x50")

        find_label = tk.Label(find_popup, text="Find:")
        find_label.pack(side='left', padx=10)

        find_entry = tk.Entry(find_popup, width=25)
        find_entry.pack(side='left', fill='x', expand=True)

        find_button = tk.Button(find_popup, text="Find", command=lambda: self.highlight_text(find_entry.get()))
        find_button.pack(side='left', padx=10)

    def highlight_text(self, text_to_find):
        self.text_area.tag_remove('highlight', '1.0', tk.END)
        if text_to_find:
            start_pos = '1.0'
            while True:
                start_pos = self.text_area.search(text_to_find, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(text_to_find)}c"
                self.text_area.tag_add('highlight', start_pos, end_pos)
                start_pos = end_pos
            self.text_area.tag_config('highlight', background='yellow')

    def change_theme(self, theme):
        if theme == 'light':
            self.text_area.config(bg='white', fg='black')
        elif theme == 'dark':
            self.text_area.config(bg='black', fg='white')

if __name__ == "__main__":
    root = tk.Tk()
    editor = BasicaEditor(root)
    root.mainloop()