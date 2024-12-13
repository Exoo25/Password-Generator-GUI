import customtkinter as ctk
import secrets
import string

# Function to generate the password
def generate_password():
    try:
        length = int(length_entry.get())  # Get password length from the entry
        if length < 4:
            result_label.config(text="Password length must be at least 4 characters.", fg="red")
            return
    except ValueError:
        result_label.config(text="Please enter a valid number.", fg="red")
        return

    # Create password from a combination of letters, digits, and punctuation
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))

    # Update the password entry with the generated password
    password_entry.delete(0, ctk.END)
    password_entry.insert(0, password)

    # Update result label
    result_label.config(text="Password generated successfully.", fg="green")

# Create main window using customtkinter
root = ctk.CTk()
root.title("Modern Password Generator")
root.geometry("400x300")

# Set appearance mode to "dark"
ctk.set_appearance_mode("dark")

# Create and place label for password length
length_label = ctk.CTkLabel(root, text="Enter Password Length:")
length_label.pack(pady=10)

# Create and place entry for password length
length_entry = ctk.CTkEntry(root, placeholder_text="e.g. 12", width=150)
length_entry.pack(pady=5)

# Create and place button to generate password
generate_button = ctk.CTkButton(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=20)

# Create and place label to show result (password)
password_label = ctk.CTkLabel(root, text="Generated Password:")
password_label.pack(pady=10)

# Create and place entry to display generated password
password_entry = ctk.CTkEntry(root, width=250)
password_entry.pack(pady=5)

# Create and place result label
result_label = ctk.CTkLabel(root, text="", width=250)
result_label.pack(pady=5)

# Run the application
root.mainloop()
