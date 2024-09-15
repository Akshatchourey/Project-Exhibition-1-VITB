import mysql.connector
from Authorization import Author
import App
user_id = "entry"
# The program starts its execution from here, connection is established with database.
# for security purposes host, password, user and database name is removed.
if __name__ == "__main__":
    db = mysql.connector.connect(host='localhost', password='12345akshat', user='root', database="money")
    courser = db.cursor()
    if db.is_connected(): print("Connection successfully...")

    user_id = "abcdefgh"
    author = Author(user_id)
    author.mainloop()

    print(user_id)
    app = App.App(user_id)
    app.mainloop()
    db.close()
 