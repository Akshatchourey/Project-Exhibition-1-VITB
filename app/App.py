from imports import tk
from imports import ttk
from Home import HomePage
from Add import AddPage
from Analyse import AnalysePage

# This class is responsible for creating main
# window with menu buttons, container and 4 frames for 4 different pages
class App(tk.Tk):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        user_id = "asdf"
        self.title("College Transactions")
        self.iconbitmap("logo.ico")
        self.geometry("990x615+175+90")
        self.minsize(900,550)
        self.bind('<Escape>', lambda event: self.quit())

        style = ttk.Style()
        style.configure("TButton",font=('', 11), width=20)
        menu = ttk.Frame(self, borderwidth=4)
        menu.pack(side='left', fill='y')

        title = ttk.Label(menu, text="College Transactions", font="Helvetica 15 bold")
        home = ttk.Button(menu, text="Home Page", command=lambda: self.show_frame(HomePage))
        add = ttk.Button(menu, text="Data Page", command=lambda: self.show_frame(AddPage))
        analyse = ttk.Button(menu, text="Analysis Page", command=lambda: self.show_frame(AnalysePage))

        title.pack()
        home.pack()
        add.pack()
        analyse.pack()

        container = ttk.Frame(self)
        container.pack(side="top", expand=True, fill="both")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # first time creating frame and storing in frames list
        self.frames = {}

        for F in {HomePage, AddPage, AnalysePage}:
            frame = F(self, container, self.user_id)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    # simple function to lift the frame on top
    def show_frame(self, frame):
        self.frames[frame].tkraise()
