import tkinter as tk
from tkinter import filedialog

def execute_script():
    # Получение данных из текстовых полей
    data1 = entry1.get()
    data2 = entry2.get()
    folder_path = folder_var.get()
    print(data1)
    print(data2)
    print(folder_path)
    
    # Здесь можно запустить ваш скрипт, передав переменные data1, data2 и folder_path в качестве аргументов

# Создание главного окна
root = tk.Tk()
root.title("Пример GUI")

# Создание текстовых полей
label1 = tk.Label(root, text="Данные 1:", height=5, width=15)

label1.grid(row=0, column=0)
entry1 = tk.Entry(root, width=25)
entry1.grid(row=0, column=1)
frame1 = tk.Frame(root, width=25)
frame1.grid(row=0, column=2)

label2 = tk.Label(root, text="Данные 2:")
label2.grid(row=1, column=0)
entry2 = tk.Entry(root, width=25)
entry2.grid(row=1, column=1)
frame2 = tk.Frame(root, width=25)
frame2.grid(row=1, column=2)

frame3 = tk.Frame(root, height=25, width=25)
frame3.grid(row=2, column=0)


# Кнопка для выбора пути к папке
def choose_folder():
    folder_selected = filedialog.askdirectory()
    folder_var.set(folder_selected)
    label3 = tk.Label(root, text=f"Выбранная директория: {folder_var.get()}")
    label3.grid(row=2, column=1)

folder_var = tk.StringVar()
folder_button = tk.Button(root, text="Выбрать папку", command=choose_folder)
folder_button.grid(row=3, column=0, columnspan=2)

# Кнопка выполнения
execute_button = tk.Button(root, text="Выполнить", command=execute_script)
execute_button.grid(row=4, column=0, columnspan=2)

root.mainloop()
