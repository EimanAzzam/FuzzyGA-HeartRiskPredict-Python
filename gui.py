import tkinter as tk

f = open("data.txt", "r")
dAta = [float(line) for line in f.readlines()]

print(dAta)

def calculate_risk():
    # Get the values entered by the user
    input_values = [float(entry.get()) for entry in entries]
    for i in range(5):
        input_values[i] = input_values[i] * dAta[i]
        dAta.append(input_values)

    total = sum(input_values)
    return total

def submit():
    risk = calculate_risk()
    result_label.config(text=f"Risk Value: {risk}")

# Create the main window
root = tk.Tk()
root.title("Heart Attack Disease Checker")
root.geometry("1024x720")
root.iconbitmap("icon.ico")
root.configure(bg="black")  # Set background to black

# Load the background image
background_image = tk.PhotoImage(file="background_image.png")

# Create a label for the background image
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a label for the title
title_label = tk.Label(root, text="Heart Attack Risk Detection", font=("Sans serif", 35), bg="black", fg="white", bd=2, relief="flat")
title_label.place(relx=0.5, y=50, anchor="center")

# Create labels and entry fields for each input
labels = ["Age:", "Cholestrol\nlevel:", "Blood\npressure:", "Heart Rate\nper minute:", "Exercise\nHours:", "BMI:"]
entries = []

for i, label_text in enumerate(labels):
    font_size = 20 if label_text == "Age:" else 12  # Set font size to 20 for "Age" label, 12 for others
    label = tk.Label(root, text=label_text, font=("Arial", font_size), anchor="w", bg="black", fg="white", bd=2, relief="flat")
    label.place(x=50, y=150 + i * 50)

    entry = tk.Entry(root, font=("Arial", 20))
    entry.place(x=200, y=150 + i * 50)

    entries.append(entry)

# Create a label to display the risk value
result_label = tk.Label(root, text="Risk \nof heart attack : ", anchor="w", bg="black", fg="white", font=("Arial", 20), bd=2, relief="flat")
result_label.place(x=50, y=450)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit, bg="red", fg="white", font=("Arial", 20), bd=2, relief="flat")
submit_button.place(relx=1.0, x=-50, y=500, anchor="e")

# Start the Tkinter event loop
root.mainloop()
