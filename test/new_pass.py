import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk 

verification_code = None
current_username = None  
user_passwords = {"shoryapathak07@gmail.com": "password"} 

def reset_password(entered_code, new_password, confirm_password):
    global current_username, verification_code
    if entered_code == verification_code:
        if new_password == confirm_password:
            user_passwords[current_username] = new_password
            messagebox.showinfo("Success", "Password reset successful!")
            root.destroy()

        else:
            messagebox.showerror("Error", "Passwords do not match!")
    else:
        messagebox.showerror("Error", "Invalid verification code!")

def enter_new_password_page():
    global root
    root = tk.Tk()
    root.title("Enter New Password Page")
    root.geometry("500x450")

    background_image = Image.open("img2.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    canvas = tk.Canvas(root, width=500, height=450)
    canvas.pack(fill="both", expand=True)

    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    style = ttk.Style()
    style.configure("TButton", font=('', 11), width=20)
    style.map("TButton", foreground=[("active", "white")], background=[("active", "#3498db")])

    label_heading = ttk.Label(root, text="Enter New Password", font=("Helvetica", 18, "bold"))
    label_heading.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    verification_code_label = ttk.Label(root, text="Verification Code: ", font=("Arial", 12))
    verification_code_label.place(relx=0.3, rely=0.3, anchor=tk.CENTER)

    verification_code_entry = ttk.Entry(root, font=("Arial", 12), width=20)
    verification_code_entry.place(relx=0.6, rely=0.3, anchor=tk.CENTER)

    new_password_label = ttk.Label(root, text="New Password: ", font=("Arial", 12))
    new_password_label.place(relx=0.3, rely=0.4, anchor=tk.CENTER)

    new_password_entry = ttk.Entry(root, font=("Arial", 12), show="*", width=20)
    new_password_entry.place(relx=0.6, rely=0.4, anchor=tk.CENTER)

    confirm_password_label = ttk.Label(root, text="Confirm Password: ", font=("Arial", 12))
    confirm_password_label.place(relx=0.3, rely=0.5, anchor=tk.CENTER)

    confirm_password_entry = ttk.Entry(root, font=("Arial", 12), show="*", width=20)
    confirm_password_entry.place(relx=0.6, rely=0.5, anchor=tk.CENTER)

    submit_button = ttk.Button(root, text="Submit", command=lambda: reset_password(verification_code_entry.get(), new_password_entry.get(), confirm_password_entry.get()))
    submit_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    root.mainloop()

enter_new_password_page()
