import mysql.connector
from Authorization import Author
import App

# The program starts its execution from here, connection is established with database.
# for security purposes host, password, user and database name is removed.
if __name__ == "__main__":
    user_id = "abcdefgh"
    author = Author()
    author.mainloop()

    print(user_id)
    app = App.App(user_id)
    app.mainloop()
 