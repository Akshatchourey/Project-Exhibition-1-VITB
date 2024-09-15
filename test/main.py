import mysql.connector
import numpy as np
from Database import Abc

if __name__ == "__main__":
    db = mysql.connector.connect(host='localhost', password='12345akshat', user='root', database="money")
    courser = db.cursor()
    if db.is_connected():
        print("Connection successfully...")

    arr_2D = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]])

    obj = Abc(db)
    db.close()
