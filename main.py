import tkinter as tk
from tkinter import messagebox

# Create window
window = tk.Tk()
window.title("Student Study Planner")
window.geometry("600x500")

# Title
title = tk.Label(
    window,
    text="Student Study Planner",
    font=("Arial", 22, "bold")
)
title.pack(pady=20)

# Subject
tk.Label(window, text="Subject").pack()
subject_entry = tk.Entry(window, width=40)
subject_entry.pack(pady=5)

# Topic
tk.Label(window, text="Topic").pack()
topic_entry = tk.Entry(window, width=40)
topic_entry.pack(pady=5)

# Date
tk.Label(window, text="Study Date").pack()
date_entry = tk.Entry(window, width=40)
date_entry.pack(pady=5)

# Priority
tk.Label(window, text="Priority").pack()

priority = tk.StringVar()
priority.set("Medium")

priority_menu = tk.OptionMenu(
    window,
    priority,
    "High",
    "Medium",
    "Low"
)
priority_menu.pack(pady=5)


# Add task function
def add_task():

    subject = subject_entry.get()
    topic = topic_entry.get()
    date = date_entry.get()
    level = priority.get()

    if subject == "" or topic == "" or date == "":
        messagebox.showwarning(
            "Warning",
            "Please enter all details"
        )
        return

    task = (
        subject
        + " | "
        + topic
        + " | "
        + date
        + " | Priority: "
        + level
    )

    task_list.insert(tk.END, task)

    subject_entry.delete(0, tk.END)
    topic_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)


# Delete task function
def delete_task():

    selected = task_list.curselection()

    if selected:
        task_list.delete(selected)
    else:
        messagebox.showwarning(
            "Warning",
            "Please select a task"
        )


# Add button
add_button = tk.Button(
    window,
    text="Add Study Task",
    command=add_task,
    width=20
)
add_button.pack(pady=10)


# Task list
tk.Label(
    window,
    text="My Study Tasks",
    font=("Arial", 14, "bold")
).pack(pady=10)

task_list = tk.Listbox(
    window,
    width=75,
    height=8
)
task_list.pack(pady=5)


# Delete button
delete_button = tk.Button(
    window,
    text="Delete Selected Task",
    command=delete_task,
    width=20
)
delete_button.pack(pady=10)


# Start application
window.mainloop()