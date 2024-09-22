from imports import ttk
from imports import Image, ImageTk
from imports import database

# This class is for analyzing the data.
class ProfilePage(ttk.Frame):

    def __init__(self, parent, container, table):
        super().__init__(container)
        self.table = table
        self.courser = database().cursor()
        ttk.Label(self, text="Profile Page", font=('Times', '20')).pack()

        # your --- code here
