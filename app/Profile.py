from imports import ttk
from imports import Image, ImageTk

# This class is for analyzing the data.
class AnalysePage(ttk.Frame):
    def __init__(self, parent, container, user_id):
        super().__init__(container)
        self.user_id = user_id
        ttk.Label(self, text="Profile Page", font=('Times', '20')).pack()
        # code here

