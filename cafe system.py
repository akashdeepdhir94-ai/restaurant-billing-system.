import tkinter as tk
from tkinter import messagebox

# Menu dictionary
menu = { 
    'pizza': 34,
    'pasta': 78,
    'chicken': 123,
    'burger': 80,
    'coffee': 45
}

# Initialize order list
ordered_items = []

# Function to add item to the order
def add_item():
    item = item_var.get().lower()
    qty = qty_var.get()
    
    if item not in menu:
        messagebox.showerror("Error", f"'{item}' is not on the menu!")
        return
    
    if not qty.isdigit() or int(qty) <= 0:
        messagebox.showerror("Error", "Enter a valid quantity!")
        return
    
    qty = int(qty)
    ordered_items.append((item, qty))
    messagebox.showinfo("Added", f"Added {qty} x {item} to order")
    qty_var.set("")
    item_var.set("")

# Function to generate final bill
def generate_bill():
    if not ordered_items:
        messagebox.showwarning("No items", "No items ordered yet!")
        return
    
    bill_text.delete(1.0, tk.END)
    bill_text.insert(tk.END, "="*40 + "\n")
    bill_text.insert(tk.END, " " * 10 + "Indian Restaurant\n")
    bill_text.insert(tk.END, "="*40 + "\n")
    bill_text.insert(tk.END, f"{'Item':15}{'Qty':5}{'Price':10}{'Total':10}\n")
    bill_text.insert(tk.END, "-"*40 + "\n")
    
    total_amount = 0
    for item, qty in ordered_items:
        price = menu[item]
        total_price = price * qty
        total_amount += total_price
        bill_text.insert(tk.END, f"{item.capitalize():15}{qty:<5}₹{price:<10}₹{total_price:<10}\n")
    
    bill_text.insert(tk.END, "-"*40 + "\n")
    bill_text.insert(tk.END, f"{'Grand Total':30}₹{total_amount:<10}\n")
    bill_text.insert(tk.END, "="*40 + "\n")
    bill_text.insert(tk.END, "Thank you for dining with us! 🍴\n")
    bill_text.insert(tk.END, "="*40 + "\n")

# Main GUI window
root = tk.Tk()
root.title("Indian Restaurant Billing System")
root.geometry("500x500")

# Item selection
tk.Label(root, text="Enter Item Name:").pack(pady=5)
item_var = tk.StringVar()
tk.Entry(root, textvariable=item_var).pack(pady=5)

# Quantity
tk.Label(root, text="Enter Quantity:").pack(pady=5)
qty_var = tk.StringVar()
tk.Entry(root, textvariable=qty_var).pack(pady=5)

# Add button
tk.Button(root, text="Add Item", command=add_item).pack(pady=10)

# Generate bill button
tk.Button(root, text="Generate Bill", command=generate_bill).pack(pady=10)

# Text area for bill
bill_text = tk.Text(root, height=15, width=55)
bill_text.pack(pady=10)

# Run the GUI
root.mainloop()