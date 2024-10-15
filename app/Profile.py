from imports import tk, ttk
from imports import db, database

# This class is Profile page
class ProfilePage(ttk.Frame):

    def __init__(self, parent, container, table):
        super().__init__(container)
        self.table = table
        self.courser = db.cursor()
        self.courser.execute("select userName,fullName,balanceOn,balanceOf,goal,spent,averageM,bio,email"
                             " from pro where userId=%s", table)
        asq = list(self.courser.fetchone().values())

        style = ttk.Style()
        style.configure('TLabel', font=('', 15), width=13)

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

        ttk.Label(f1, text=asq[0], font=('Times', 25)).pack(anchor='nw',pady=80)
        ttk.Label(f1, text=asq[1] + ", ", font=('Times', 17)).pack(side='left', anchor='nw',fill=tk.X)
        ttk.Label(f1, text=asq[8], font=('Times', 17)).pack(side='left', anchor='nw',fill=tk.X, expand=True)
        ttk.Label(f21, text="Bio").pack()
        ttk.Label(f21, text=asq[7]).pack(fill=tk.X)

        ttk.Label(f22, text="Balance: ").grid(row=0, column=0)
        ttk.Label(f22, text=asq[2]+asq[3], foreground='blue').grid(row=0, column=1)
        ttk.Label(f22, text="Goal: ").grid(row=1, column=0)
        ttk.Label(f22, text=asq[4], foreground='green').grid(row=1, column=1)
        ttk.Label(f22, text="Spent: ").grid(row=2, column=0)
        ttk.Label(f22, text=asq[5], foreground='red').grid(row=2, column=1)
        ttk.Label(f22, text=" ").grid(row=3, column=0)
        ttk.Label(f22, text="Current Average: ").grid(row=4, column=0)
        ttk.Label(f22, text=asq[6], foreground='blue').grid(row=4, column=1)
