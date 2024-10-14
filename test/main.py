import numpy as np
from datetime import datetime
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import io

if __name__ == "__main__":
    # arr_2D = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    print("main program")
    #
    # aks = tk.Tk()
    #
    # img = open("testImage.jpg", "rb")
    # bImg = img.read()
    #
    # image = Image.open(io.BytesIO(bImg)).resize((150,150))
    # photo_image = ImageTk.PhotoImage(image)
    # canvas = tk.Canvas(aks, width=200, height=200)
    # canvas.pack()
    # canvas.create_image(100, 100, image=photo_image)
    #
    # aks.mainloop()

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(time)
