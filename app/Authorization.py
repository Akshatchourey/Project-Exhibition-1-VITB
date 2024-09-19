import os
import random
import smtplib
import pymysql
from imports import tk
from imports import ttk
from dotenv import load_dotenv

import Personalize

# Authorization
class Author(tk.Tk):
    def __init__(self):
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

        ttk.Button(self, text="login", command=lambda: self.click_log()).pack()
        ttk.Button(self, text="forgot password?", command=lambda: Author.rase_frame(parent, Forgotpass)).pack()
        ttk.Button(self, text="new account", command=lambda: Author.rase_frame(parent, Signin)).pack()

    def click_log(self):
        # username and password
        username = "test_user"
        password = "123aks123"
        try:
            timeout = 10
            db = pymysql.connect(
                charset="utf8mb4",
                connect_timeout=timeout,
                cursorclass=pymysql.cursors.DictCursor,
                db="money",
                host=os.environ.get('DB_HOST'),
                password=password,
                read_timeout=timeout,
                port=12727,
                user=username,
                write_timeout=timeout,
            )
            print("Connection successfully...")

        except pymysql.Error as e:
            print("invalid credentials.")

class Signin(ttk.Frame, Author):
    def __init__(self, parent, container):
        self.parent = parent
        super().__init__(container)
        ttk.Label(self, text="Signin", font=('Times', '20')).pack()
        ttk.Button(self, text="Go Back", command=lambda: Author.rase_frame(parent, Login)).pack()
        ttk.Button(self, text="Sign in", command=lambda:  self.click_sign()).pack()

    def click_sign(self):
        new_username = "test_user1"
        new_password = "123aks123"
        user_id = "van2"
        # try:
        #     timeout = 10
        #     db = pymysql.connect(
        #         charset="utf8mb4",
        #         connect_timeout=timeout,
        #         cursorclass=pymysql.cursors.DictCursor,
        #         db="money",
        #         host=os.environ.get('DB_HOST'),
        #         password=os.environ.get('DB_PASSWORD_ROOT'),
        #         read_timeout=timeout,
        #         port=12727,
        #         user=os.environ.get('DB_USER_ROOT'),
        #         write_timeout=timeout,
        #     )
        #     print("Connection successfully...")
        #
        # except pymysql.Error as e:
        #     print(f"Connection failed: {e}")
        #
        # courser = db.cursor()
        # courser.execute("""CREATE TABLE "van2" (
        #   "SNo" int NOT NULL,
        #   "Date" date DEFAULT NULL,
        #   "Note" varchar(250) NOT NULL,
        #   "Type" varchar(125) DEFAULT NULL,
        #   "Mode" tinyint(1) DEFAULT NULL,
        #   "Amount" decimal(7,2) DEFAULT NULL,
        #   PRIMARY KEY ("SNo")
        # )""")
        # print("new user is created.")
        # db.close()

        # courser.execute("CREATE USER %s@%s IDENTIFIED BY %s;", (new_username,'%', new_password))
        # courser.execute("GRANT SELECT, INSERT ON money.%s TO %s@%s;" % (user_id, new_username,'%'))
        # courser.commit()

        personalize = Personalize.PersonalizePage()
        personalize.mainloop()

        Author.rase_frame(self.parent, Login)

class Forgotpass(ttk.Frame, Author):
    def __init__(self, parent, container):
        super().__init__(container)
        ttk.Label(self, text="forgot password", font=('Times', '20')).pack()
        code = str(random.randint(1000, 9999))
        ttk.Button(self, text="Send Code", command=lambda: self.send_code(code)).pack()

    def send_code(self, code):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        print(code)
        server.ehlo()
        server.starttls()
        server.login("shoryapathak07@gmail.com", "Shorya9528**!!?", initial_response_ok=True)
        server.sendmail("shoryapathak07@gmail.com", "achourey09@gmail.com",code)
        server.quit()
        Author.rase_frame(parser, Verify)

class Verify(ttk.Frame, Author):
    def __init__(self, parent, container):
        super().__init__(container)
        ttk.Label(self, text="Verify", font=('Times', '20')).pack()
        ttk.Button(self, text="verify", command=lambda: Author.rase_frame(parent, Login)).pack()


if __name__ == "__main__":
    load_dotenv()
    author = Author()
    author.mainloop()
