from imports import *

from App import App
from Personalize import PersonalizePage

# Authorization
class Author(tk.Tk):
    def __init__(self):
        super().__init__()
        self.user_id = "entry"
        self.title("Authorize yourself")
        self.geometry("500x450+175+90")
        self.iconbitmap("logo.ico")
        container = ttk.Frame(self)
        container.pack(side="top", expand=True, fill="both")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # first time creating frame and storing in frames list
        self.frames = {}
        for F in {Login, Signup, Forgotpass, Verify}:
            frame = F(self, container)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.rase_frame(Login)

    def rase_frame(self, curr_frame):
        self.frames[curr_frame].tkraise()

class Login(ttk.Frame, Author):
    def __init__(self, parent, container):
        super().__init__(container)
        self.parent = parent
        # ttk.Label(self, text="Login", font=('Times', '20')).pack()
        self.login_user_value = tk.StringVar(value="Vanshika")
        self.login_pass_value = tk.StringVar(value="123456789")

        # login --- your code

        ttk.Button(self, text="login", command=lambda: self.click_log()).pack()
        ttk.Button(self, text="forgot password?", command=lambda: Author.rase_frame(parent, Forgotpass)).pack()
        ttk.Button(self, text="new account", command=lambda: Author.rase_frame(parent, Signup)).pack()

    def click_log(self):
        # username and password
        username = self.login_user_value.get()
        password = self.login_pass_value.get()
        f = switch_user(username, password)
        if f == 0:
            courser.execute("select userId from pro where userName='%s'" % username)
            global table_name
            table_name = courser.fetchone()['userId']
            Author.destroy(self.parent)


class Signup(ttk.Frame, Author):
    def __init__(self, parent, container):
        self.db = None
        self.courser = None
        self.parent = parent
        super().__init__(container)
        ttk.Label(self, text="Signin", font=('Times', '20')).pack()
        self.sign_user_value = tk.StringVar(value="Vanshika")
        self.sign_email_value = tk.StringVar(value="achourey09@gmail.com")
        self.sign_pass_value = tk.StringVar(value="123456789")

        # Sign up --- your code

        ttk.Button(self, text="Go Back", command=lambda: Author.rase_frame(parent, Login)).pack()
        ttk.Button(self, text="Sign in", command=lambda:  self.click_sign()).pack()

    def click_sign(self):
        new_username = self.sign_user_value.get()
        new_email = self.sign_email_value.get()
        new_password = self.sign_pass_value.get()
        Author.rase_frame(self.parent, Login)
        try:
            self.db = pymysql.connect(
                charset="utf8mb4",
                connect_timeout=timeout,
                cursorclass=pymysql.cursors.DictCursor,
                db="money",
                host=os.environ.get('DB_HOST'),
                password=os.environ.get('DB_PASSWORD_ROOT'),
                read_timeout=timeout,
                port=12727,
                user=os.environ.get('DB_USER_ROOT'),
                write_timeout=timeout,
            )
            print("Connection successfully...")

        except pymysql.Error as e:
            print(f"Connection failed: {e}")

        user_id = "van258"
        self.courser = self.db.cursor()
        # self.courser.execute("""CREATE TABLE '%s' ("SNo" int NOT NULL,"Date" date,"Note" varchar(250) NOT NULL,
        #   "Type" varchar(125),"Mode" tinyint(1),"Amount" decimal(7,2) NOT NULL,PRIMARY KEY ("SNo"));""" % user_id)

        # self.courser.execute("select max(SNo) from pro;")
        # sno = self.courser.fetchone()['max(SNo)']+1
        # new_user_row = (sno, user_id, new_username, new_password, "test@gmail.com")
        # self.courser.execute("insert into pro(SNo, userId, userName, password, email) values(%s,%s,%s,%s,%s);",new_user_row)
        # self.courser.execute("create user %s@%s identified by %s;", (new_username,'%', new_password))
        # self.courser.execute("GRANT SELECT, INSERT ON money.%s TO %s@'%s';" % (user_id, new_username,'%'))

        # *messagebox
        print("new user is created.")
        # Author.withdraw(self.parent)
        personalize = PersonalizePage()
        personalize.mainloop()
        personalize.quit()
        # query_save_personal = asd()
        # print(query_save_personal)
        # Author.deiconify(self.parent)

class Forgotpass(ttk.Frame, Author):
    code = random.randint(1000, 9999)

    def __init__(self, parent, container):
        super().__init__(container)
        self.parent = parent
        ttk.Label(self, text="forgot password", font=('Times', '20')).pack()
        self.verify_user_value = tk.StringVar(value="Akshat")
        self.verify_email_value = tk.StringVar(value="choureyakshat916@gmail.com")

        # forgot --- you code

        ttk.Button(self, text="Send Code", command=lambda: self.send_code(str(self.code))).pack()

    def send_code(self, code):
        to = self.verify_email_value.get()
        user = self.verify_user_value.get()
        try:
            courser.execute("select email from pro where userName='%s';" % user)
        except None:
            print("user is not present in database")
            return

        if courser.fetchone()['email'] != to:
            # *messagebox
            print("user entered dint matches email")
            return

        f = send_mail(to, "Your verification code is ", code)
        if f == 0:
            # *messagebox
            print("Verification code has been sent to your user email address successfully.")
            Author.rase_frame(self.parent, Verify)
        else:
            # *messagebox
            print("Unable to send the email.")


class Verify(ttk.Frame, Author):
    def __init__(self, parent, container):
        super().__init__(container)
        self.parent = parent
        ttk.Label(self, text="Verify", font=('Times', '20')).pack()
        self.verify_code_value = tk.IntVar(value=Forgotpass.code)

        # verify --- your code

        ttk.Button(self, text="verify", command=lambda: self.now_verify()).pack()

    def now_verify(self):
        if self.verify_code_value.get() == Forgotpass.code:
            Author.rase_frame(self.parent, Login)

            # print(Forgotpass.forgot_user)
            # courser.execute("select email, password from pro where userName='%s';" % Forgotpass.forgot_user)
            # email = courser.fetchone()['email']
            # password = courser.fetchone()['password']
            #
            # send_mail(email,"your password", password)
            # *messagebox
            print("your password has been sent to your email address.")
        else:
            # *messagebox
            print("Incorrect code entered.")


def send_mail(to,subject, message):
    g_username = os.environ.get('G_USERNAME')
    g_password = os.environ.get('G_PASSWORD')

    msg = MIMEMultipart()
    msg['From'] = g_username
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    try:
        server = SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user=g_username, password=g_password)
        server.sendmail(from_addr=g_username, to_addrs=to, msg=msg.as_string())
        server.close()
        return 0
    except NameError:
        return 1


if __name__ == "__main__":
    courser = db.cursor()
    table_name = ""

    author = Author()
    author.mainloop()
    author.quit()

    if table_name != "":
        app = App(table_name)
        app.mainloop()
