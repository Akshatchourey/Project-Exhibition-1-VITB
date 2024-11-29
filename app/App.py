from io import BytesIO
from imports import tk, ttk
from imports import Image, ImageTk, ImageDraw
from imports import db

from Home import HomePage
from Add import AddPage
from Profile import ProfilePage
from Analyse import AnalysePage

# This class is responsible for creating main
# window with menu buttons, container and 4 frames for 4 different pages
class App(tk.Tk):
    def __init__(self, table):
        super().__init__()
        self.title("College Transactions")
        self.iconbitmap("logo.ico")
        self.geometry("990x615+175+90")
        self.minsize(900,550)
        self.bind('<Escape>', lambda event: self.quit())

        self.table = table
        self.courser = db.cursor()
        style = ttk.Style()
        style.configure("TButton",font=('', 11), width=20)
        style.configure('TLabel', font=('', 15))

        self.photo_image = self.get_profile_image()
        menu = ttk.Frame(self, borderwidth=4)
        menu.pack(side='left', fill='y')

        title = ttk.Label(menu, text="College Transactions", font="Helvetica 15 bold", width=False)
        home = ttk.Button(menu, text="Home Page", command=lambda: self.show_frame(HomePage))
        profile = ttk.Button(menu, text="Profile Page", command=lambda: self.show_frame(ProfilePage))
        add = ttk.Button(menu, text="Data Page", command=lambda: self.show_frame(AddPage))
        analyse = ttk.Button(menu, text="Analysis Page", command=lambda: self.show_frame(AnalysePage))

        title.pack()
        home.pack()
        profile.pack()
        add.pack()
        analyse.pack()

        frame2 = ttk.Frame(menu)
        frame2.pack(side='bottom', pady=40)

        self.balance = tk.DoubleVar()
        self.onl_balance = tk.DoubleVar()
        self.off_balance = tk.DoubleVar()
        self.goal = tk.DoubleVar()
        self.spent = tk.DoubleVar()
        self.get_balance()

        ttk.Label(frame2, text="Balance Onl: ").grid(row=0, column=0)
        ttk.Label(frame2, textvariable=self.onl_balance, foreground='blue').grid(row=0, column=1)
        ttk.Label(frame2, text="Balance Off: ").grid(row=1, column=0)
        ttk.Label(frame2, textvariable=self.off_balance, foreground='blue').grid(row=1, column=1)
        ttk.Label(frame2, text="Goal: ").grid(row=2, column=0)
        ttk.Label(frame2, textvariable=self.goal, foreground='green').grid(row=2, column=1)
        ttk.Label(frame2, text="Spent: ").grid(row=3, column=0)
        ttk.Label(frame2, textvariable=self.spent, foreground='red').grid(row=3, column=1)

        container = ttk.Frame(self)
        container.pack(side="top", expand=True, fill="both")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # first time creating frame and storing in frames list
        self.frames = {}

        for F in {HomePage,ProfilePage,AddPage,AnalysePage}:
            frame = F(self, container, table)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    # simple function to lift the frame on top
    def show_frame(self, frame):
        self.frames[frame].tkraise()

    def get_balance(self):
        self.courser.execute("select balanceOn,balanceOf,goal,spent from pro where userId=%s", self.table)
        data = self.courser.fetchone()
        self.onl_balance.set(data["balanceOn"])
        self.off_balance.set(data["balanceOf"])
        self.goal.set(data["goal"])
        self.spent.set(data["spent"])
        self.balance.set(self.onl_balance.get() + self.off_balance.get())

    def get_profile_image(self):
        self.courser.execute("select image from proImg where userId=%s", self.table)
        bImg = self.courser.fetchone()['image']
        print("fetching done")
        # Image for profile page
        image = Image.open(BytesIO(bImg)).resize((150, 150), Image.LANCZOS)
        mask = Image.new("L", image.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, 150, 150), fill=255)
        masked_image = Image.new("RGBA", image.size)
        masked_image.paste(image, (0, 0), mask)
        return ImageTk.PhotoImage(masked_image)
