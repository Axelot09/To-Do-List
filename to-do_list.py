import tkinter as tk
from tkinter import messagebox

# Function to add task
def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete selected task
def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Function to mark task as completed
def complete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected_task_index)
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(tk.END, f"{task} - Completed")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to mark as completed.")

# Setting up the main window
root = tk.Tk()
root.title("To-Do List")

# Frame for task entry and buttons
entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)

# Entry widget for task input
task_entry = tk.Entry(entry_frame, width=40)
task_entry.pack(side=tk.LEFT, padx=10)

# Button to add task
add_task_button = tk.Button(entry_frame, text="Add Task", command=add_task)
add_task_button.pack(side=tk.LEFT)

# Listbox to display tasks
tasks_listbox = tk.Listbox(root, width=50, height=15)
tasks_listbox.pack(pady=10)

# Frame for action buttons
action_frame = tk.Frame(root)
action_frame.pack(pady=10)

# Button to delete selected task
delete_task_button = tk.Button(action_frame, text="Delete Task", command=delete_task)
delete_task_button.pack(side=tk.LEFT, padx=10)

# Button to mark task as completed
complete_task_button = tk.Button(action_frame, text="Complete Task", command=complete_task)
complete_task_button.pack(side=tk.LEFT, padx=10)

# Start the main event loop
root.mainloop()