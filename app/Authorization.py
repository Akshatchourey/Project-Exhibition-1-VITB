from imports import tk
from imports import ttk

# Authorization
class Author(tk.Tk):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = "entry"
        self.title("Authorize yourself")
        self.geometry("230x230+175+90")
        container = ttk.Frame(self)
        container.pack(side="top", expand=True, fill="both")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # first time creating frame and storing in frames list
        self.frames = {}
        for F in {Login, Signin, Forgotpass, Verify}:
            frame = F(self, container)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.rase_frame(Login)

    def rase_frame(self, curr_frame):
        self.frames[curr_frame].tkraise()

class Login(ttk.Frame, Author):
    def __init__(self, parent, container):
        super().__init__(container)
        ttk.Label(self, text="Login", font=('Times', '20')).pack()

        ttk.Button(self, text="login", command=lambda: self.login()).pack()
        ttk.Button(self, text="forgot password?", command=lambda: Author.rase_frame(parent, Forgotpass)).pack()
        ttk.Button(self, text="new account", command=lambda: Author.rase_frame(parent, Signin)).pack()

    def login(self):
        pass

class Signin(ttk.Frame, Author):
    def __init__(self, parent, container):
        super().__init__(container)
        ttk.Label(self, text="Signin", font=('Times', '20')).pack()
        ttk.Button(self, text="Sign in", command=lambda: Author.rase_frame(parent, Login)).pack()

class Forgotpass(ttk.Frame, Author):
    def __init__(self, parent, container):
        super().__init__(container)
        ttk.Label(self, text="forgot password", font=('Times', '20')).pack()
        ttk.Button(self, text="Send Code", command=lambda: Author.rase_frame(parent, Verify)).pack()

class Verify(ttk.Frame, Author):
    def __init__(self, parent, container):
        super().__init__(container)
        ttk.Label(self, text="Verify", font=('Times', '20')).pack()
        ttk.Button(self, text="verify", command=lambda: Author.rase_frame(parent, Login)).pack()
