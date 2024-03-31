import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

class FileExplorer:
    def __init__(self, root):
        self.root = root
        self.root.title("File Explorer")
        self.current_path = os.getcwd()
        self.create_widgets()

    def create_widgets(self):
        # Buttons
        self.open_button = tk.Button(self.root, text="Open File", command=self.open_file)
        self.open_button.pack()

        self.copy_button = tk.Button(self.root, text="Copy File", command=self.copy_file)
        self.copy_button.pack()

        self.rename_button = tk.Button(self.root, text="Rename File", command=self.rename_file)
        self.rename_button.pack()

        self.move_button = tk.Button(self.root, text="Move File", command=self.move_file)
        self.move_button.pack()

        self.delete_button = tk.Button(self.root, text="Delete File", command=self.delete_file)
        self.delete_button.pack()

        self.create_folder_button = tk.Button(self.root, text="Create Folder", command=self.create_folder)
        self.create_folder_button.pack()

        self.delete_folder_button = tk.Button(self.root, text="Delete Folder", command=self.delete_folder)
        self.delete_folder_button.pack()

        self.list_files_button = tk.Button(self.root, text="List Files", command=self.list_files)
        self.list_files_button.pack()

    def open_file(self):
        file_path = filedialog.askopenfilename(initialdir=self.current_path)
        if file_path:
            os.startfile(file_path)

    def copy_file(self):
        file_path = filedialog.askopenfilename(initialdir=self.current_path)
        if file_path:
            destination = filedialog.askdirectory(initialdir=self.current_path)
            shutil.copy(file_path, destination)

    def rename_file(self):
        file_path = filedialog.askopenfilename(initialdir=self.current_path)
        if file_path:
            new_name = filedialog.askstring("Rename File", "Enter new name:")
            if new_name:
                os.rename(file_path, os.path.join(os.path.dirname(file_path), new_name))

    def move_file(self):
        file_path = filedialog.askopenfilename(initialdir=self.current_path)
        if file_path:
            destination = filedialog.askdirectory(initialdir=self.current_path)
            shutil.move(file_path, destination)

    def delete_file(self):
        file_path = filedialog.askopenfilename(initialdir=self.current_path)
        if file_path:
            os.remove(file_path)

    def create_folder(self):
        folder_name = filedialog.askstring("Create Folder", "Enter folder name:")
        if folder_name:
            os.mkdir(os.path.join(self.current_path, folder_name))

    def delete_folder(self):
        folder_path = filedialog.askdirectory(initialdir=self.current_path)
        if folder_path:
            shutil.rmtree(folder_path)

    def list_files(self):
        files = os.listdir(self.current_path)
        messagebox.showinfo("Files in Folder", "\n".join(files))

if __name__ == "__main__":
    root = tk.Tk()
    app = FileExplorer(root)
    root.mainloop()