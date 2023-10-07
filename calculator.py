import tkinter as tk

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self,a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero."
        else:
            return a / b

    def power(self,a, exponent):
        result = 1

        if exponent == 0:
            return 1
        elif exponent == 1:
            return a
        elif exponent == -1:
            return 1 / a
        else:
            if exponent < 0:
                a = 1 / a
                exponent *= -1

            for i in range(exponent):
                result *= a

        return result

def perform_addition():
    a = float(entry1.get())
    b = float(entry2.get())
    result = c1.add(a, b)
    input_label.config(text=f"{a} + {b}")
    result_label.config(text="="+str(result))

def perform_subtraction():
    a = float(entry1.get())
    b = float(entry2.get())
    result = c1.subtract(a, b)
    input_label.config(text=f"{a} - {b}")
    result_label.config(text="="+str(result))

def perform_multiplication():
    a = float(entry1.get())
    b = float(entry2.get())
    result = c1.multiply(a, b)
    input_label.config(text=f"{a} * {b}")
    result_label.config(text="="+str(result))

def perform_division():
    a = float(entry1.get())
    b = float(entry2.get())
    result = c1.divide(a, b)
    input_label.config(text=f"{a} / {b}")
    result_label.config(text="="+str(result))

def perform_power():
    a = float(entry1.get())
    b = int(entry2.get())
    result = c1.power(a, b)
    input_label.config(text=f"{a} ^ {b}")
    result_label.config(text="="+str(result))


root = tk.Tk()
root.title("CodSoft Calculator")

c1 = Calculator()

entry1 = tk.Entry(root, width=20)
entry2 = tk.Entry(root, width=20)

result_label = tk.Label(root, font=(12))

input_label = tk.Label(root, text="", font=(12))


addition_button = tk.Button(root, text="+", command=perform_addition)
subtraction_button = tk.Button(root, text="-", command=perform_subtraction)
multiplication_button = tk.Button(root, text="*", command=perform_multiplication)
division_button = tk.Button(root, text="/", command=perform_division)
power_button = tk.Button(root, text="^", command=perform_power)


label1 = tk.Label(root, text="Enter value 1:")
label2 = tk.Label(root, text="Enter value 2:")


label1.grid(row=0, column=0, padx=10, pady=10)
entry1.grid(row=1, column=0, padx=10, pady=10)
label2.grid(row=2, column=0, padx=10, pady=10)
entry2.grid(row=3, column=0, padx=10, pady=10)

addition_button.grid(row=1, column=1, padx=10, pady=10)
subtraction_button.grid(row=1, column=2, padx=10, pady=10)
multiplication_button.grid(row=2, column=1, padx=10, pady=10)
division_button.grid(row=2, column=2, padx=10, pady=10)
power_button.grid(row=3, column=1, columnspan=4, padx=10, pady=10)
input_label.grid(row=5, column=0, columnspan=4, padx=10, pady=10)
result_label.grid(row=5, column=1, columnspan=4, padx=10, pady=10)


root.mainloop()