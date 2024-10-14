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

        style = ttk.Style()
        style.configure("TButton",font=('', 11), width=20)
        courser = db.cursor()
        courser.execute("select image from proImg where userId=%s", table)
        bImg = courser.fetchone()['image']
        print("fetching done")
        # Image for profile page
        image = Image.open(BytesIO(bImg)).resize((150, 150), Image.LANCZOS)
        mask = Image.new("L", image.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, 150, 150), fill=255)
        masked_image = Image.new("RGBA", image.size)
        masked_image.paste(image, (0, 0), mask)
        self.photo_image = ImageTk.PhotoImage(masked_image)

        menu = ttk.Frame(self, borderwidth=4)
        menu.pack(side='left', fill='y')

        title = ttk.Label(menu, text="College Transactions", font="Helvetica 15 bold")
        home = ttk.Button(menu, text="Home Page", command=lambda: self.show_frame(HomePage))
        profile = ttk.Button(menu, text="Profile Page", command=lambda: self.show_frame(ProfilePage))
        add = ttk.Button(menu, text="Data Page", command=lambda: self.show_frame(AddPage))
        analyse = ttk.Button(menu, text="Analysis Page", command=lambda: self.show_frame(AnalysePage))

        title.pack()
        home.pack()
        profile.pack()
        add.pack()
        analyse.pack()

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
