import tkinter as tk
from tkinter import filedialog

def execute_script():
    # Получение данных из текстовых полей
    data1 = entry_order.get()
    data2 = entry_lo.get()
    folder_path = folder_var.get()
    print(data1)
    print(data2)
    print(folder_path)

# Создание главного окна
root = tk.Tk()
root.title("QPSK модуляция")

# Создание текстовых полей
label_order = tk.Label(root, text="Порядок модуляции:", height=3)
label_order.grid(row=0, column=0)
entry_order = tk.Entry(root, width=25)
entry_order.grid(row=0, column=1)
frame1 = tk.Frame(root, width=25)
frame1.grid(row=0, column=2)

label_discret = tk.Label(root, text="Частота дискретизации:", height=3)
label_discret.grid(row=1, column=0)
entry_discret = tk.Entry(root, width=25)
entry_discret.grid(row=1, column=1)
frame2 = tk.Frame(root, width=25)
frame2.grid(row=1, column=2)

label_lo = tk.Label(root, text="Частота дискретизации:", height=3)
label_lo.grid(row=2, column=0)
entry_lo = tk.Entry(root, width=25)
entry_lo.grid(row=2, column=1)
frame3 = tk.Frame(root, width=25)
frame3.grid(row=2, column=2)

label_noise = tk.Label(root, text="Уровень добавляемого к сигналу шума:", height=3)
label_noise.grid(row=3, column=0)
entry_noise = tk.Entry(root, width=25)
entry_noise.grid(row=3, column=1)
frame4 = tk.Frame(root, width=25)
frame4.grid(row=3, column=2)

label_period = tk.Label(root, text="Период передачи данных:", height=3)
label_period.grid(row=4, column=0)
entry_period = tk.Entry(root, width=25)
entry_period.grid(row=4, column=1)
frame5 = tk.Frame(root, width=25)
frame5.grid(row=4, column=2)

frame4 = tk.Frame(root, height=25, width=25)
frame4.grid(row=5, column=0)

# Кнопка для выбора пути к папке
def choose_folder():
    folder_selected = filedialog.askopenfilename()
    folder_var.set(folder_selected)
    label3 = tk.Label(root, text=f"Выбранная директория: {folder_var.get()}")
    label3.grid(row=5, column=0, columnspan=2)

folder_var = tk.StringVar()
folder_button = tk.Button(root, text="Выбрать файл", command=choose_folder)
folder_button.grid(row=6, column=0, columnspan=2)

# Кнопка выполнения
execute_button = tk.Button(root, text="Выполнить", command=execute_script)
execute_button.grid(row=7, column=0, columnspan=2)

root.mainloop()
