import tkinter as tk
import math

def button_click(item):
    display_var.set(display_var.get() + str(item))

def button_clear():
    display_var.set("")

def button_equal():
    try:
        expr = display_var.get()
        expr += ')' * (expr.count('(') - expr.count(')'))
        expr = expr.replace('^', '**')
        
        math_dict = {
            'sin': lambda x: round(math.sin(math.radians(x)), 10),
            'cos': lambda x: round(math.cos(math.radians(x)), 10),
            'tan': lambda x: round(math.tan(math.radians(x)), 10),
            'sqrt': math.sqrt
        }
        
        result = str(eval(expr, {"__builtins__": None}, math_dict))
        
        if result.endswith('.0'):
            result = result[:-2]
            
        display_var.set(result)
    except Exception:
        display_var.set("Error")

root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("360x520")
root.configure(bg='#2f3640')

display_var = tk.StringVar()
display = tk.Entry(root, textvariable=display_var, font=('Arial', 24, 'bold'), bg='#f5f6fa', fg='#2f3640', justify='right')
display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, pady=15)

buttons = [
    ('sin', 1, 0), ('cos', 1, 1), ('tan', 1, 2), ('sqrt', 1, 3),
    ('(', 2, 0), (')', 2, 1), ('^', 2, 2), ('/', 2, 3),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*', 3, 3),
    ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('-', 4, 3),
    ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('+', 5, 3),
    ('C', 6, 0), ('0', 6, 1), ('.', 6, 2), ('=', 6, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, font=('Arial', 18, 'bold'), bg='#4cd137', fg="white", command=button_equal)
    elif text == 'C':
        btn = tk.Button(root, text=text, font=('Arial', 18, 'bold'), bg='#e84118', fg="white", command=button_clear)
    elif text in ('sin', 'cos', 'tan', 'sqrt'):
        btn = tk.Button(root, text=text, font=('Arial', 14, 'bold'), bg='#7f8fa6', fg="white", command=lambda t=text: button_click(t + '('))
    elif text in ('/', '*', '-', '+', '^', '(', ')'):
        btn = tk.Button(root, text=text, font=('Arial', 18, 'bold'), bg='#e1b12c', fg="white", command=lambda t=text: button_click(t))
    else:
        btn = tk.Button(root, text=text, font=('Arial', 18, 'bold'), bg='#353b48', fg="white", command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col, sticky="nsew", padx=3, pady=3)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(1, 7):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
