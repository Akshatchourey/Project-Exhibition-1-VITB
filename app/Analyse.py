from imports import ttk
from imports import Figure
from imports import FigureCanvasTkAgg

# This class is for analyzing the data.
class AnalysePage(ttk.Frame):
    def __init__(self, parent, container, user_id):
        super().__init__(container)
        self.user_id = user_id
        label = ttk.Label(self, text="Analyzing Page", font=('Times', '20'))
        frame3 = ttk.Frame(self)
        label.pack()
        frame3.pack()
        dect = {
            "food":"select Amount from entry where Type ='food' order by Date;",
            "small entries":"select Amount from entry where Amount>-500 and Amount<500 order by Date;",
            "all entries":"select Amount from entry order by Date;"
        }
        ttk.Button(frame3, command=lambda: self.clear_graph(), text="Clear Graph").pack()
        box1 = ttk.Button(frame3, text="food", command=lambda: self.graph(dect.get("food"), "food"))
        box2 = ttk.Button(frame3, text="small entries", command=lambda: self.graph(dect.get("small entries"),"small entries"))
        box3 = ttk.Button(frame3, text="all entries", command=lambda: self.graph(dect.get("all entries"),"all entries"))
        box1.pack(side='left')
        box2.pack(side='left')
        box3.pack(side='left')

        self.fig = Figure(figsize=(7, 6), dpi=110)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(expand=True,fill='both',padx=20, pady=20)
        self.plt = self.fig.add_subplot(111)

    def clear_graph(self):
        self.fig.clf()
        self.plt = self.fig.add_subplot(111)
        self.canvas.draw()

    def graph(self, query, legend):
        courser.execute(query)
        x_axis, values = [], []
        data = courser.fetchall()
        x_axis = [i for i in range(len(data))]
        for t in data: values.append(t[0])

        self.plt.plot(x_axis, values, label=legend)
        self.plt.set_title("Graph")
        self.plt.set_ylabel("Amount")
        self.plt.set_xlabel("Entries")
        self.plt.legend()
        self.canvas.draw()
