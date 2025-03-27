import tkinter as tk
from tkinter import messagebox
import hashlib
import re

def check_password_strength(password):
    """Evaluate password strength based on different character rules."""
    strength = 0
    
    if len(password) >= 8:
        strength += 1

    if re.search(r'[A-Z]', password):
        strength += 1

    if re.search(r'[a-z]', password):
        strength += 1

    if re.search(r'\d', password):
        strength += 1

    if re.search(r'[@$!%*?&]', password):
        strength += 1

    if strength <= 2:
        return "Weak"
    elif strength == 3:
        return "Moderate"
    else:
        return "Strong"

def hash_password(password):
    """Hash the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def analyze_password():
    """Analyze the entered password and display strength and hash."""
    password = entry.get()
    
    if not password:
        messagebox.showwarning("Warning", "Please enter a password!")
        return
    
    strength = check_password_strength(password)
    hashed_pw = hash_password(password)
    
    result_label.config(text=f"🔒 Strength: {strength}\n\n🔑 SHA-256 Hash:\n{hashed_pw}")

root = tk.Tk()
root.title("Password Analyzer")
root.geometry("400x250") 
root.resizable(False, False)  

tk.Label(root, text="🔐 Password Strength Analyzer", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Enter Password:", font=("Arial", 10)).pack()
entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack()

tk.Button(root, text="Analyze", font=("Arial", 10), command=analyze_password).pack(pady=10)

result_label = tk.Label(root, text="", wraplength=350, justify="left", font=("Arial", 10))
result_label.pack()

root.mainloop()
