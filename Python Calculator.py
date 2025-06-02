import tkinter as tk


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)


expression = ""
entry_text = tk.StringVar()

def press(key):
    global expression
    expression += str(key)
    entry_text.set(expression)

def clear():
    global expression
    expression = ""
    entry_text.set("")

def equal():
    global expression
    try:
        result = str(eval(expression))
        entry_text.set(result)
        expression = result
    except:
        entry_text.set("Error")
        expression = ""


entry = tk.Entry(root, textvariable=entry_text, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
    ('C',5,0)
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=equal)
    elif text == 'C':
        btn = tk.Button(root, text=text, padx=85, pady=20, font=("Arial", 14), command=clear)
        btn.grid(row=row, column=col, columnspan=4)
        continue
    else:
        btn = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=lambda t=text: press(t))
    btn.grid(row=row, column=col)


root.mainloop()
