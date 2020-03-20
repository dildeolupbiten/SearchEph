# -*- coding: utf-8 -*-

from .modules import tk


class Label(tk.Label):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack()
        self.var = tk.StringVar()
        self.var.set("None")
        self.configure(textvariable=self.var)


class LabelField(tk.Frame):
    def __init__(
            self,
            texts: tuple = (),
            title: str = "",
            *args,
            **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.pack(fill="x", expand=True)
        self.configure(bd=1, relief="sunken")
        self.texts = texts
        self.title_label = tk.Label(
            master=self,
            text=title,
            font="Default 12 bold"
        )
        self.title_label.pack()
        self.frame = tk.Frame(master=self)
        self.frame.pack()
        self.create_labels(texts=self.texts)
        self.create_labels(texts=(":",) * 3)
        self.variables = self.create_variables(n=3)
        self.sign = next(self.variables)
        self.position = next(self.variables)
        self.date = next(self.variables)

    def create_labels(self, texts: tuple = ()):
        frame = tk.Frame(master=self.frame)
        frame.pack(side="left")
        for i, j in enumerate(texts):
            label = tk.Label(
                master=frame,
                text=j,
                font="Default 11 bold"
            )
            label.grid(row=i, column=0, sticky="nw")

    def create_variables(self, n: int = 0):
        frame = tk.Frame(master=self.frame)
        frame.pack(side="left")
        for i in range(n):
            yield Label(master=frame)

