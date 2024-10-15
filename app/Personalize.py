import io
from imports import os
from imports import Client
from imports import tk, ttk
from imports import datetime
from imports import load_dotenv
from imports import Image, ImageTk
from tkinter.filedialog import askopenfilename
from imports import db

class PersonalizePage(tk.Tk):
    def __init__(self, table):
        super().__init__()
        self.table = table
        self.title("Personalize Page")
        self.iconbitmap("logo.ico")
        self.geometry("890x515+175+90")
        self.rowconfigure((0,1), weight=1)
        self.columnconfigure((0,1), weight=1)
        style = ttk.Style()
        style.configure("TLabel", font=('', 12))

        ttk.Label(self, text="Personalize Page", font=('Times', '20')).pack()
        ttk.Label(self, text="Pl scan this qr code, send message to use our whatsapp services.").pack()
        # placeholders
        person_f1 = ttk.Frame(self)
        person_f2 = ttk.Frame(self)
        person_f1.pack(side='left')
        person_f2.pack()

        self.file = tk.StringVar(value="")
        fName_value = tk.StringVar()
        phone_value = tk.StringVar(value="+91")
        balanceOn_value = tk.DoubleVar()
        balanceOf_value = tk.DoubleVar()
        goal_value = tk.IntVar()

        qr_image = Image.open("whatsapp QR.jpg").resize((200, 200), Image.LANCZOS)
        self.photo_image = ImageTk.PhotoImage(image=qr_image)
        canvas = tk.Canvas(person_f1, width=200, height=200)
        canvas.create_image((100, 100), image=self.photo_image)
        canvas.pack(anchor='center')

        ttk.Button(person_f2, text="Upload photo", command=lambda: self.upload_file()).grid(row=0,column=0)
        ttk.Label(person_f2, textvariable=self.file, width=20).grid(row=0, column=1)
        ttk.Label(person_f2, text="Full Name: ").grid(row=1, column=0)
        ttk.Entry(person_f2, textvariable=fName_value).grid(row=1, column=1)
        ttk.Label(person_f2, text="Phone No: ").grid(row=2, column=0)
        ttk.Entry(person_f2, textvariable=phone_value).grid(row=2, column=1)
        ttk.Label(person_f2, text="Balance Online: ").grid(row=3, column=0)
        ttk.Entry(person_f2, textvariable=balanceOn_value).grid(row=3, column=1)
        ttk.Label(person_f2, text="Balance Offline: ").grid(row=4, column=0)
        ttk.Entry(person_f2, textvariable=balanceOf_value).grid(row=4, column=1)
        ttk.Label(person_f2, text="This month goal: ").grid(row=5, column=0)
        ttk.Entry(person_f2, textvariable=goal_value).grid(row=5, column=1)
        ttk.Label(person_f2, text="Bio: ").grid(row=6,column=0)
        text_box = tk.Text(person_f2, width=45, height=10)
        text_box.grid(row=7, column=0, columnspan=3)

        ttk.Button(person_f2, text="Save", command=lambda: self.save_data(
            fName_value,phone_value,balanceOn_value,balanceOf_value,goal_value,
            text_box.get("1.0",'end-1c'))).grid(row=8, column=0, columnspan=2)

    def upload_file(self):
        f_types = [('Jpg Files', '*.jpg'), ('Png files','*.png')]
        file = askopenfilename(filetypes=f_types)
        self.file.set(file)

    def save_data(self,fName_value,phone_value,balanceOn_value,balanceOf_value,goal_value, text_box):
        # first message by twilio
        load_dotenv()
        account_sid = os.environ.get('Twilio_sid')
        auth_token = os.environ.get('Twilio_token')
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body="""Welcome to our WhatsApp services.
To add your transactions efficiently use the following formate:

"Note" "mode:onl/off" "amount"

Ex- "english event" onl 250

Use sync button in add transition page to update entries. Thank you""",
            to=f'whatsapp:{phone_value.get()}'
        )

        courser = db.cursor()
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        row = (fName_value.get(), phone_value.get(), text_box,balanceOn_value.get(),
               balanceOf_value.get(), goal_value.get(), time, self.table)
        courser.execute("update pro set fullName=%s, phoneNo=%s, bio=%s, balanceOn=%s,"
                        "balanceOf=%s, goal=%s, lastSync=%s where userId=%s;", row)
        if self.file.get() == "": self.file.set("testImage.jpg")
        img = open(self.file.get(), "rb").read()
        courser.execute("select max(SNo) from proImg;")
        temp_no = courser.fetchone()['max(SNo)'] + 1
        courser.execute("insert into proImg values(%s,%s,%s);", (temp_no, self.table, img))
        db.commit()

        print("Saving...personal data.")
        self.destroy()
        self.quit()
