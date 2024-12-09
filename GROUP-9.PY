#PASSWORD GENERATOR
#Performed by :-Cdt.Ayush Ranjan(3787),Cdt.Arshit Sharma(3786),Cdt.Pratyush Chamail(3769),Cdt.Saksham Garla(3792)
import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate password
def generate_password(length=4, include_special_chars=True):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits  # Letters (upper + lower) + digits
    
    if include_special_chars:
        characters += string.punctuation  # Add special characters
    
    # Randomly select characters from the pool to create the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Function to be called when the "Generate" button is pressed
def generate():
    try:
        # Get user input for password length
        length = int(entry_length.get())
        if length < 1:
            raise ValueError("Length must be a positive integer")
        
        # Get the checkbox status for including special characters
        include_special = var_special.get()
        
        # Generate password
        password = generate_password(length, include_special)
        
        # Display the generated password
        label_result.config(text=f"Generated Password: {password}")
    
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets
label_length = tk.Label(root, text="Password Length:")
label_length.pack(pady=5)

entry_length = tk.Entry(root)
entry_length.pack(pady=5)
entry_length.insert(0, "8")  # Default length is 8 characters

var_special = tk.BooleanVar(value=True)
checkbox_special = tk.Checkbutton(root, text="Include Special Characters", variable=var_special)
checkbox_special.pack(pady=5)

button_generate = tk.Button(root, text="Generate Password", command=generate)
button_generate.pack(pady=10)

label_result = tk.Label(root, text="Generated Password: ")
label_result.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()


