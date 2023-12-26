import tkinter as tk  # Импортируем модуль tkinter для создания графического интерфейса
from tkinter import ttk  # Импортируем модуль ttk из tkinter для создания виджета Progressbar
from math import atan  # Импортируем функцию atan (арктангенс) из модуля math

# Определение функции
def func(x):  # Определяем функцию, которая принимает один аргумент x
    return atan(2*x + 1)  # Возвращаем значение функции y = arctan(2x + 1)

# Определение процедуры табулирования
def tabulate(start, end, step):  # Определяем процедуру табулирования, которая принимает три аргумента: начало, конец и шаг табулирования
    x = start  # Начинаем с начального значения
    while x <= end:  # Пока x не превысит конечное значение
        y = func(x)  # Вычисляем значение функции
        listbox.insert(tk.END, f"x = {x:.2f}, y = {y:.2f}")  # Добавляем строку с текущими значениями x и y в конец Listbox
        progress['value'] += step  # Увеличиваем значение Progressbar на величину шага
        window.update_idletasks()  # Обновляем окно, чтобы отобразить изменения
        x += step  # Увеличиваем x на величину шага

# Создание окна
window = tk.Tk()  # Создаем новое окно
window.title("Табулирование функции")  # Устанавливаем заголовок окна

# Создание виджетов
progress = ttk.Progressbar(window, orient="horizontal", length=300, mode="determinate")  # Создаем виджет Progressbar
listbox = tk.Listbox(window, width=30, height=20)  # Создаем виджет Listbox
button = tk.Button(window, text="Начать", command=lambda: tabulate(0.01, 0.9, 0.01))  # Создаем кнопку, которая при нажатии вызывает процедуру табулирования

# Размещение виджетов
progress.pack(pady=10)  # Размещаем Progressbar в окне
listbox.pack(pady=10)  # Размещаем Listbox в окне
button.pack(pady=10)  # Размещаем кнопку в окне

window.mainloop()  # Запускаем главный цикл обработки событий