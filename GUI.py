import tkinter as tk
from mood import detect

root = tk.Tk()

# Create a label and entry widget for the user to input a statement
label = tk.Label(root, text="Enter a statement:",font=('Arial', 20), fg='blue')
label.pack()
entry = tk.Entry(root, width=30)
entry.pack()

# Define a function to store the statement entered by the user
def store_statement():
    statement = entry.get()
    detect(statement)
# Create a button to allow the user to store the statement
button = tk.Button(root, text="Enter", command=store_statement, height=2, width=10)
button.pack()

root.mainloop()
