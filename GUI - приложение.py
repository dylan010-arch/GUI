import tkinter as tk
from tkinter import ttk, messagebox, filedialog

class MyApplication:
    def __init__(self, master):
        self.master = master
        master.title("Мое приложение")
        master.geometry("600x400")
        master.configure(bg="#e6e6e6")  

        self.create_widgets()
        self.create_menu()

    def create_widgets(self):
        self.label = ttk.Label(self.master, text="Привет, Tolagay!", font=("Arial", 14, "bold"), background="#e6e6e6")
        self.label.pack(pady=20)

        self.entry = ttk.Entry(self.master, font=("Arial", 12))
        self.entry.pack(pady=10)

        self.button_show_message = ttk.Button(self.master, text="Показать сообщение", command=self.show_message)
        self.button_show_message.pack(pady=10)

        self.text_area = tk.Text(self.master, wrap="word", width=40, height=10, font=("Arial", 12))
        self.text_area.pack(pady=10)

        self.button_back = ttk.Button(self.master, text="Очистить", command=self.clear_text_area)
        self.button_back.pack(pady=10)

    def create_menu(self):
        menu_bar = tk.Menu(self.master)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Открыть", command=self.on_file_open)
        file_menu.add_command(label="Сохранить", command=self.on_file_save)
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=self.master.destroy)

        settings_menu = tk.Menu(menu_bar, tearoff=0)
        settings_menu.add_command(label="Настройки", command=self.show_settings_dialog)

        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Справка", command=self.show_help)

        menu_bar.add_cascade(label="Файл", menu=file_menu)
        menu_bar.add_cascade(label="Настройки", menu=settings_menu)
        menu_bar.add_cascade(label="Справка", menu=help_menu)

        self.master.config(menu=menu_bar)

    def show_message(self):
        user_input = self.entry.get()
        self.label.config(text=f"Привет, {user_input}!")
        messagebox.showinfo("Сообщение", f"Привет, {user_input}!")

    def on_file_open(self):
        file_path = filedialog.askopenfilename(title="Открыть файл", filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)

    def on_file_save(self):
        file_path = filedialog.asksaveasfilename(title="Сохранить файл", defaultextension=".txt", filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)

    def show_settings_dialog(self):
        settings_dialog = tk.Toplevel(self.master)
        settings_dialog.title("Настройки")

    def show_help(self):
        messagebox.showinfo("Справка", "Дополнительная информация по использованию приложения.")

    def clear_text_area(self):
        self.text_area.delete(1.0, tk.END)

root = tk.Tk()
app = MyApplication(root)
root.mainloop()
