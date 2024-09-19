from imports import tk
from imports import ttk

class PersonalizePage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("College Transactions")
        self.iconbitmap("logo.ico")
        self.geometry("890x515+175+90")
        self.bind('<Escape>', lambda event: self.quit())
        ttk.Label(self, text="Personalize Page").pack()
        ttk.Button(self, text="Save", command=lambda: self.save_data()).pack()

    def save_data(self):
        # save
        pass
