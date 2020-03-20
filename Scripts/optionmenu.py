# -*- coding: utf-8 -*-

from .modules import tk


class OptionMenu(tk.OptionMenu):
    def __init__(self, master=None, values=None):
        self.var = tk.StringVar()
        super().__init__(master, self.var, *("", *values))
        self.configure(width=8)
        self.pack()


class OptionFrame(tk.Frame):
    def __init__(
            self,
            text: str = "",
            side: str = "",
            values=None,
            *args,
            **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.pack(side=side)
        self.label = tk.Label(master=self, text=text, font="Default 12 bold")
        self.label.pack()
        self.optionmenu = OptionMenu(master=self, values=values)

