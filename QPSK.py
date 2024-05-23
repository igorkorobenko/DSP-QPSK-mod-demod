import tkinter as tk
from tkinter import filedialog
import random
import numpy as np
import math
import matplotlib.pyplot as plt

def execute_script(entry_order, entry_samplerate, entry_noise, entry_lo, folder_var):
    # Получение данных из текстовых полей
    mod_order = int(entry_order.get())
    # fs = int(entry_samplerate.get())
    # lo = int(entry_lo.get())
    # noise = int(entry_noise.get())
    # folder_path = folder_var.get()
    print(mod_order)
    # print(fs)
    # print(lo)
    # print(noise)
    # print(folder_path)
    # qpsk_mod(mod_order, fs, lo, noise, folder_path)
    qpsk_mod(mod_order) 

def qpsk_mod(mod_order, fs=0, lo=0, noise=0, folder_path=0):
    data = [random.randint(0, 1) for _ in range(50)]
    print(data)
    stem_plot(data)

    # Разделение массива на четные и нечетные индексы
    # even_index_data = []
    # odd_index_data = []
    # is_even = True  
    # for num in data_transformed:
    #     if is_even:
    #         even_index_data.append(num)
    #         is_even = False
    #     else:
    #         odd_index_data.append(num)
    #         is_even = True

    # Проверка длины массивов
    # if len(even_index_data) > len(odd_index_data):
    #     even_index_data = even_index_data[:-1]  # Удалить последний элемент, если четных больше
    data = data[:-(len(data) % mod_order)]
    order_dim_array = np.reshape(data, (-1, mod_order))

    print(order_dim_array)
    # Создание двумерного массива
    # order_dim_array = np.column_stack((odd_index_data, even_index_data))

    # задаем массив отсчетов
    # ts = np.arange(0, 1000/fs, 1/fs)

    # bit_t = 200
    # a = np.repeat(two_dim_array, bit_t)

    # data_gray = gray_encode(data)
    # data_transformed = data_gray
    # for i in range(len(data)):
    #     data_transformed[i] = 2*data_gray[i]-1
    # print(data_transformed)


    # for i in range (len(data)/2):


def gray_encode(binary_sequence):
    gray_sequence = [binary_sequence[0]]
    for i in range(1, len(binary_sequence)):
        gray_bit = binary_sequence[i-1] ^ binary_sequence[i]
        gray_sequence.append(gray_bit)
    return gray_sequence

def stem_plot(data):
    # Построение stem-графика
    plt.figure(figsize=(10, 4))
    markerline, stemlines, baseline = plt.stem(data)
    plt.setp(markerline, 'markerfacecolor', 'b')

    plt.title('Stem-график данных (0 и 1)')
    plt.xlabel('Индекс')
    plt.ylabel('Значение')
    plt.yticks([0, 1])  # Установка меток на оси Y для значений 0 и 1
    plt.grid(True)
    # plt.show()

def interface():
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

    label_samplerate = tk.Label(root, text="Частота дискретизации:", height=3)
    label_samplerate.grid(row=1, column=0)
    entry_samplerate = tk.Entry(root, width=25)
    entry_samplerate.grid(row=1, column=1)
    frame2 = tk.Frame(root, width=25)
    frame2.grid(row=1, column=2)

    label_lo = tk.Label(root, text="Несущая частота:", height=3)
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
    execute_button = tk.Button(root, text="Выполнить", command=execute_script(entry_order, entry_samplerate,
                                                                              entry_noise, entry_lo, folder_var))
    execute_button.grid(row=7, column=0, columnspan=2)

    root.mainloop()


def main():
    # interface()
    # execute_script(4, 1000000,5, 200000, 0)
    qpsk_mod(8, 1000000,5, 200000, 0) 

if __name__ == "__main__":
    main()


