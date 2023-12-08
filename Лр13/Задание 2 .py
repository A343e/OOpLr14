import tkinter as tk
from tkinter import messagebox
import random

class ArrayApp:
    def __init__(self, wn):
        self.root = wn
        self.root.title("Array Application")

        self.label = tk.Label(wn, text="Введите размер массива:")
        self.label.pack()

        self.entry = tk.Entry(wn)
        self.entry.pack()

        self.button_generate = tk.Button(wn, text="Сгенерировать массив", command=self.generate_array)
        self.button_generate.pack()

        self.array_label = tk.Label(wn, text="Массив:")
        self.array_label.pack()

        self.result_label = tk.Label(wn, text="")
        self.result_label.pack()

    def generate_array(self):
        try:
            size = int(self.entry.get())
            if size <= 0:
                messagebox.showerror("Ошибка", "Размер массива должен быть положительным числом.")
                return

            array = [random.randint(1, 100) for _ in range(size)]
            array_str = ", ".join(map(str, array))
            self.array_label.config(text="Массив: " + array_str)

            min_element = min(array)
            max_element = max(array)
            sum_elements = sum(array)

            result_str = f"Минимальный элемент: {min_element}\nМаксимальный элемент: {max_element}\nСумма элементов: {sum_elements}"
            self.result_label.config(text=result_str)

        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректное целое число для размера массива.")

if __name__ == "__main__":
    wn = tk.Tk()
    app = ArrayApp(wn)
    wn.mainloop()