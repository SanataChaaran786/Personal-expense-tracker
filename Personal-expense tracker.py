import tkinter as tk
from tkinter import messagebox
import csv
import os

FILE_NAME = "expenses.csv"

def add_expense():
    expense = f"{date_entry.get()} - {category_entry.get()} - Rs. {amount_entry.get()}"
    if not all([date_entry.get(), category_entry.get(), amount_entry.get()]):
        return messagebox.showwarning("Warning", "Fill all fields!")
    
    try:
        float(amount_entry.get())  # Validate amount
    except ValueError:
        return messagebox.showwarning("Warning", "Amount must be a number!")
    
    expense_list.insert(tk.END, expense)
    with open(FILE_NAME, "a", newline="") as file:
        csv.writer(file).writerow(expense.split(" - "))
    
    date_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for row in csv.reader(file):
                expense_list.insert(tk.END, f"{row[0]} - {row[1]} - Rs. {row[2]}")
                
def delete_expense():
    try:
        expense_list.delete(expense_list.curselection()[0])
    except IndexError:
        messagebox.showwarning("Warning", "Select an expense to delete!")
root = tk.Tk()
root.title("Expense Tracker")
date_entry, category_entry, amount_entry = tk.Entry(root), tk.Entry(root), tk.Entry(root)
for label, entry in zip(["Date:", "Category:", "Amount:"], [date_entry, category_entry, amount_entry]):
    tk.Label(root, text=label).pack()
    entry.pack()
tk.Button(root, text="Add Expense", command=add_expense).pack()
tk.Button(root, text="Delete Expense", command=delete_expense).pack()
expense_list = tk.Listbox(root, width=50)
expense_list.pack()
load_expenses()
root.mainloop()
