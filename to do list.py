import tkinter as tk
from tkinter import messagebox, simpledialog

tasks = []

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def edit_task():
    try:
        selected = listbox.curselection()[0]
        current_task = tasks[selected]
        new_task = simpledialog.askstring("Edit Task", "Edit the selected task:", initialvalue=current_task)
        if new_task:
            tasks[selected] = new_task
            update_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to edit.")

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Saved", "Tasks saved to tasks.txt")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            loaded = file.read().splitlines()
            global tasks
            tasks = loaded
            update_listbox()
    except FileNotFoundError:
        pass


root = tk.Tk()
root.title("To-Do List App")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry = tk.Entry(frame, width=40)
entry.pack(side=tk.LEFT, padx=5)

add_btn = tk.Button(frame, text="Add Task", command=add_task)
add_btn.pack(side=tk.LEFT)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(padx=10, pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

edit_btn = tk.Button(btn_frame, text="Edit Task", command=edit_task)
edit_btn.pack(side=tk.LEFT, padx=5)

del_btn = tk.Button(btn_frame, text="Delete Task", command=delete_task)
del_btn.pack(side=tk.LEFT, padx=5)

save_btn = tk.Button(btn_frame, text="Save Tasks", command=save_tasks)
save_btn.pack(side=tk.LEFT, padx=5)

load_btn = tk.Button(btn_frame, text="Load Tasks", command=load_tasks)
load_btn.pack(side=tk.LEFT, padx=5)


load_tasks()
root.mainloop()
