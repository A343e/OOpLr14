import tkinter as tk

def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    total_amount = principal + interest
    return total_amount

def calculate_compound_interest(principal, rate, time):
    total_amount = principal * (1 + rate / 100) ** time
    return total_amount

def calculate():
    principal = float(entry_principal.get())
    rate = float(entry_rate.get())
    time = float(entry_time.get())

    simple_interest = calculate_simple_interest(principal, rate, time)
    compound_interest = calculate_compound_interest(principal, rate, time)

    label_simple_interest_result.config(text=f"Простые проценты: {simple_interest:.2f}")
    label_compound_interest_result.config(text=f"Сложные проценты: {compound_interest:.2f}")

wn = tk.Tk()
wn.title("Вычисление дохода по вкладу")

frame = tk.Frame(wn)
frame.pack(padx=20, pady=20)

label_principal = tk.Label(frame, text="Введите начальную сумму:")
label_principal.grid(row=0, column=0)
entry_principal = tk.Entry(frame)
entry_principal.grid(row=0, column=1)

label_rate = tk.Label(frame, text="Введите процентную ставку:")
label_rate.grid(row=1, column=0)
entry_rate = tk.Entry(frame)
entry_rate.grid(row=1, column=1)

label_time = tk.Label(frame, text="Введите срок в годах:")
label_time.grid(row=2, column=0)
entry_time = tk.Entry(frame)
entry_time.grid(row=2, column=1)

button_calculate = tk.Button(frame, text="Рассчитать", command=calculate)
button_calculate.grid(row=3, columnspan=2)

label_simple_interest_result = tk.Label(frame, text="")
label_simple_interest_result.grid(row=4, columnspan=2)

label_compound_interest_result = tk.Label(frame, text="")
label_compound_interest_result.grid(row=5, columnspan=2)

wn.mainloop()
