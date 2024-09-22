from imports import tk
from imports import ttk

class PersonalizePage(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Personalize Page")
        self.iconbitmap("logo.ico")
        self.geometry("890x515+175+90")

        # code here
        ttk.Label(self, text="Personalize Page").pack()
        self.name = tk.StringVar(value="pro")
        ttk.Button(self, text="Save", command=lambda: self.save_data()).pack()

    def save_data(self):
        self.destroy()

def asd():
    return query_temp


query_temp = "hfjhguvgh"
