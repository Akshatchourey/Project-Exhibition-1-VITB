from imports import os
from imports import Client
from imports import load_dotenv
from imports import datetime, timedelta
from imports import tk, ttk, messagebox

from imports import db, database

# courser = database().cursor()
# This is the biggest and most important part...
# This class facilitates adding new data and showing past data
# this data page frame is further have 2 frames (add_f1 and add_f2).pack()
# inside add_f1 we use grid whereas in add_f2 we use pack()
class AddPage(ttk.Frame):
    def __init__(self, parent, container, table):
        super().__init__(container)
        self.table = table
        self.courser = database().cursor()
        add_t = ttk.Label(self, text="Add Transactions", font=('Times', '20'))
        add_t.pack()

        # These are placeholders for add_f1
        self.courser.execute("select max(SNo) from %s;" % table)
        # noinspection PyTypeChecker
        temp_no = self.courser.fetchone()['max(SNo)']
        if temp_no is None: temp_no = 0
        self.no = tk.IntVar(value=temp_no + 1)
        date_value = tk.StringVar(value="dd/mm/2024")
        note_value = tk.StringVar(value="note")
        type_value = tk.StringVar(value="Category")
        mode_value = tk.BooleanVar()
        amount_value = tk.DoubleVar()

        add_f1 = ttk.Frame(self)
        add_f1.pack(fill='x')
        add_f1.columnconfigure((0,1,2,3,4,5,6), weight=1)
        add_f1.rowconfigure(0, weight=1)

        # add_f1 widgets
        types = ["food","pocket money","friend/partner","stationary","events","personal","shopping","other"]
        date_entry = ttk.Entry(add_f1, textvariable=date_value)
        note_entry = ttk.Entry(add_f1, textvariable=note_value)
        type_entry = ttk.Combobox(add_f1, textvariable=type_value)
        type_entry['value'] = types
        mode_online = ttk.Radiobutton(add_f1, text="Online", value=False, variable=mode_value)
        mode_offline = ttk.Radiobutton(add_f1, text="Offline", value=True, variable=mode_value)
        amount_entry = ttk.Entry(add_f1, textvariable=amount_value)

        # griding add_f1 widgets
        ttk.Label(add_f1, font=('', 0, ''), width=0,textvariable=self.no).grid(row=0, column=0,rowspan=2, sticky='ew')
        date_entry.grid(row=0, column=1,rowspan=2, sticky='ew')
        note_entry.grid(row=0, column=2,rowspan=2, sticky='ew')
        mode_online.grid(row=0, column=3)
        mode_offline.grid(row=1, column=3)
        type_entry.grid(row=0, column=4,rowspan=2, sticky='ew')
        amount_entry.grid(row=0, column=5,rowspan=2, sticky='ew')
        add_data = ttk.Button(add_f1, text="Add Data",
                              command=lambda: self.add_data(date_value,note_value,type_value,mode_value,amount_value))
        add_data.grid(row=0, column=6, rowspan=2)

        show_t = ttk.Label(self, text="Show Transactions", font=('Times', '20'))
        show_t.pack()
        add_f2 = ttk.Frame(self)
        add_f2.pack()

        refresh = ttk.Button(add_f2, text="Refresh Data",
                             command=lambda:self.show_data("select * from %s order by Date desc;"))
        refresh.pack(side='left')

        # different qsl commands stored in dict
        dicti = {
            '2023': "select * from %s where YEAR(Date)=2023;",
            '2024': "select * from %s where YEAR(Date)=2024;",
            'Online': "select * from %s where Mode=False order by Date desc;",
            'Offline': "select * from %s where Mode=True order by Date desc;",
            'amount+': "select * from %s where Amount>0 order by Date desc;",
            'amount-': "select * from %s where Amount<0 order by Date desc;",
            'amount+desc': "select * from %s where Amount>0 order by Amount desc;",
            'amount-desc': "select * from %s where Amount<0 order by Amount;"
        }
        # making combo-box
        filters = ['2023','2024','Online','Offline','amount+','amount-','amount+desc','amount-desc']
        filter_value = tk.StringVar(value="Filters")
        combo = ttk.Combobox(add_f2, textvariable=filter_value)
        combo['values'] = filters
        combo.pack(side='left')
        combo.bind('<<ComboboxSelected>>', lambda event:self.show_data(dicti[filter_value.get()]))

        type_combo = ttk.Combobox(add_f2)
        type_combo['values'] = types
        type_combo.set("Type Filters")
        type_combo.pack(side='left')
        type_combo.bind('<<ComboboxSelected>>',
                        lambda event: self.show_data(
                            f"select * from %s where Type='{type_combo.get()}' order by Date desc;"))
        sync = ttk.Button(add_f2, text="Sync", command=lambda: self.sync_data(), width=10)
        sync.pack(side='left')

        # Creating tree view(Table) and setting initial properties of it
        self.tree = ttk.Treeview(self, columns=('sno', 'date', 'note', 'category', 'amount'), show='headings', height=5)
        self.tree.column("sno", width=50)
        self.tree.column("date", width=95)
        self.tree.column('note', width=210)
        self.tree.heading('sno', text='SNo.')
        self.tree.heading('date', text='Date')
        self.tree.heading('note', text='Note')
        self.tree.heading('category', text='Category')
        self.tree.heading('amount', text='Amount')
        self.tree.pack(expand=True,fill='both',padx=9, pady=9)
        ttk.Style().configure('Treeview', rowheight=28)
        self.tree.tag_configure("colour_blue", foreground="blue")
        self.tree.tag_configure("tree_font", font='None 13')

        self.show_data("select * from %s order by Date desc;")

    # This function takes sql query and display one-by-one in tree view
    def show_data(self, query):
        self.tree.delete(*self.tree.get_children())
        self.courser.execute(query % self.table)
        asq = [list(row.values()) for row in self.courser.fetchall()]
        i = 1
        for t in asq:
            new_date = t[1].strftime("%d/%m/%y")
            row = (i, new_date, t[2], t[3], t[5])
            if t[4]: self.tree.insert('', 'end', values=row, tags=('colour_blue',"tree_font",))
            else: self.tree.insert('', 'end', values=row, tags=("tree_font",))
            i += 1

    # This function takes few data from placeholders of add_f1 and runs sql query for insertion.
    def add_data(self, date_value, note_value, type_value, mode_value, amount_value):
        insert_query1 = "insert into %s values(%s," % (self.table, self.no.get())
        insert_query2 = ",'%s','%s',%s,%s);" % (note_value.get(), type_value.get(), mode_value.get(), amount_value.get())
        insert_query = insert_query1 + f"STR_TO_DATE('{date_value.get()}','%d/%m/%Y')" + insert_query2
        self.courser.execute(insert_query)
        database().commit()
        self.no.set(self.no.get() + 1)
        self.show_data("select * from %s order by Date desc;")

    def sync_data(self):
        courser = db.cursor()
        courser.execute("select phoneNo,lastSync from pro where userId='%s';" % self.table)
        asq = courser.fetchone()
        phoneNo = asq['phoneNo']
        date_after = asq['lastSync'] - timedelta(hours=5, minutes=30)
        load_dotenv()
        account_sid = os.environ.get('Twilio_sid')
        auth_token = os.environ.get('Twilio_token')
        client = Client(account_sid, auth_token)

        messages = client.messages.list(date_sent_after=date_after, from_=f'whatsapp:{phoneNo}')
        for msg in messages:
            dates = msg.date_sent.strftime("%Y-%m-%d")
            mess = msg.body
            body = mess.split(" ")
            mode = body[-2]
            money = body[-1]
            note = mess[:len(mess)-len(mode)-len(money)-2]
            mode = 0 if mode == "onl" else 1
            row = (self.table, self.no.get(), dates, note, "other", mode, int(money))
            self.courser.execute("insert into %s values(%s,'%s','%s','%s', %s, %s);" % row)
            self.no.set(self.no.get()+1)
        database().commit()

        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        courser.execute("update pro set lastSync='%s' where userId='%s';" % (time, self.table))
        db.commit()
        self.show_data("select * from %s order by Date desc;")

        messagebox.showinfo("Syncing", f"syncing successful with {len(messages)} more additions.")
