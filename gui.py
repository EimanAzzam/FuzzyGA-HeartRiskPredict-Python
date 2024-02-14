import tkinter as tk
import tkinter.font 

f = open("data.txt","r")
dAta=[float(line) for line in f.readlines()]

print(dAta)

def submit():
    # Get the values entered by the user
    input_values = [float(entry.get()) for entry in entries]
    for i in range(5):
        input_values[i]=input_values[i]*dAta[i]
        dAta.append(input_values)

    total = sum(input_values)
    result_label.config(text=f"Total: {total}")

# Create the main window
root = tk.Tk()
root.title("Heart attack disease checker")
root.geometry("1024x720")
root.iconbitmap("icon.ico")
# Create labels and entry fields for each input
labels = ["Input 1:", "Input 2:", "Input 3:", "Input 4:", "Input 5:"]
entries = []

for i, label_text in enumerate(labels):
    label = tk.Label(root, text=label_text, anchor="w")
    label.grid(row=i, column=0, padx=5, pady=5, sticky="w")
    
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=5, pady=5, sticky="w")
    
    entries.append(entry)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=len(labels), columnspan=2, padx=5, pady=10, sticky="we")

# Create a label to display the total
result_label = tk.Label(root, text="", anchor="w")
result_label.grid(row=len(labels)+1, columnspan=2, padx=5, pady=5, sticky="we")

# Start the Tkinter event loop
root.mainloop()
