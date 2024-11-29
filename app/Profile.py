from imports import tk, ttk, messagebox
from imports import db, database

# This class is Profile page
class ProfilePage(ttk.Frame):

    def __init__(self, parent, container, table):
        super().__init__(container)
        self.table = table
        self.courser = db.cursor()
        self.parent = parent
        self.courser.execute("select fullName,email,phoneNo,note,averageM,prediction from pro where userId=%s", table)
        asq = list(self.courser.fetchone().values())

        # your --- code here
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)
        self.columnconfigure(0,weight=1)
        f1 = ttk.Frame(self)
        f2 = ttk.Frame(self)
        f1.grid(row=0, column=0, sticky="nsew")
        f2.grid(row=1, column=0, sticky="nsew")

        f2.rowconfigure(0, weight=1)
        f2.columnconfigure(0, weight=2)
        f2.columnconfigure(1, weight=1)
        f21 = ttk.Frame(f2, relief="groove", borderwidth=2)
        f22 = ttk.Frame(f2, relief="raised", borderwidth=2)
        f21.grid(row=0, column=0, sticky="nsew", columnspan=2)
        f22.grid(row=0, column=3, sticky="nse", padx=14, pady=9)

        ttk.Label(f1, text="Profile Page", font=('Times', '20')).pack()
        canvas = tk.Canvas(f1, width=200, height=200)
        canvas.pack(side='left', anchor="nw", padx=5, pady=5)
        canvas.create_image(100, 100, image=parent.photo_image)

        ttk.Label(f1, text=f"{asq[0]}\n{asq[1]}\n{asq[2]}", font=('Times', 23)).pack(anchor='nw',pady=60)
        ttk.Label(f21, text="Note").pack()
        text_box = tk.Text(f21, height=11, width=55, font=("Helvetica", 15))
        text_box.pack()
        text_box.insert('1.0', str(asq[3]))
        ttk.Button(f21, text="Save", command=lambda:self.save_note(text_box.get("1.0", tk.END)), width=10).pack()

        ttk.Label(f22, text="Balance: ").grid(row=0, column=0)
        ttk.Label(f22, textvariable=parent.balance, foreground='blue').grid(row=0, column=1)
        ttk.Label(f22, text="Goal: ").grid(row=1, column=0)
        ttk.Label(f22, textvariable=parent.goal, foreground='green').grid(row=1, column=1)
        ttk.Label(f22, text="Spent: ").grid(row=2, column=0)
        ttk.Label(f22, textvariable=parent.spent, foreground='red').grid(row=2, column=1)
        ttk.Label(f22, text="Current Average: ").grid(row=3, column=0)
        ttk.Label(f22, text=asq[4], foreground='blue').grid(row=3, column=1)
        ttk.Label(f22, text="Prediction: ").grid(row=4, column=0)
        ttk.Label(f22, text=asq[5], foreground='blue').grid(row=4, column=1)
        ttk.Label(f22, text="",).grid(row=5, column=0)
        ttk.Label(f22, text="Set your new goal:").grid(row=6, column=0)
        ttk.Entry(f22, textvariable=parent.goal).grid(row=7, column=0)
        ttk.Button(f22, text="change", command=lambda:self.change_goal(), width=12).grid(row=7, column=1)

    def change_goal(self):
        self.courser.execute("update pro set goal=%s where userId='%s';" % (self.parent.goal.get(),self.table))
        db.commit()
        messagebox.showinfo("Goal changed", f"Goal changed\nYour new goal is {self.parent.goal.get()}.")

    def save_note(self, notes):
        self.courser.execute("update pro set note='%s' where userId='%s';" % (notes, self.table))
        db.commit()
        messagebox.showinfo("Saving..", "Your notes is successfully saved.")
