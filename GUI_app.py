import customtkinter as ctk
from tkinter import messagebox

# Function to handle button click
def on_button_click():
    user_input = entry.get()
    if user_input:
        messagebox.showinfo("Greeting", f"Hello, {user_input}!")
    else:
        messagebox.showwarning("Input Error", "Please enter your name.")

# Create the main window
ctk.set_appearance_mode("dark")  # Set the theme: "dark" or "light"
ctk.set_default_color_theme("blue")  # Set the color theme: "blue", "green", "dark-blue"

root = ctk.CTk()
root.title("Modern GUI")
root.geometry("400x300")  # Set the window size

# Add a label
label = ctk.CTkLabel(root, text="Enter your name:", font=("Arial", 16))
label.pack(pady=20)

# Add an entry widget
entry = ctk.CTkEntry(root, placeholder_text="Your Name", font=("Arial", 14))
entry.pack(pady=10)

# Add a button
button = ctk.CTkButton(root, text="Greet Me", font=("Arial", 14), command=on_button_click)
button.pack(pady=20)

# Run the application
root.mainloop()