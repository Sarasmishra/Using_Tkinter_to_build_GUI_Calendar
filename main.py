import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
def get_date():
    selected_date = cal.get_date()
    selected_date_label.config(text="The selected date is:"+selected_date)

# creating the tkinter window
root = tk.Tk()
root.title("My Calender")
root.geometry("600x600")

# creating the widget
cal = Calendar(root,selectmode="day",date_pattern="dd-mm-yyyy")
cal.pack(pady=10)

# Now defining the function
selected_date_label = ttk.Label(root,text="The selected date is:")
selected_date_label.pack(pady=5)

# Creating a button
select_button = ttk.Button(root,text="Select Date",command=get_date)
select_button.pack(pady=5)

root.mainloop()