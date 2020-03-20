# -*- coding: utf-8 -*-

from .modules import tk


class SpinboxScale:
    def __init__(
            self,
            master=None,
            digit: int = 0,
            increment: float = .0,
            _from: float = .0,
            _to: float = .0,
            text: str = "",
            title: str = "",
            textvariable: tk.DoubleVar = None,
    ):
        self.title = tk.Label(
            master=master,
            text=title,
            font="Default 12 bold"

        )
        self.title.pack()
        self.frame = tk.Frame(master=master)
        self.frame.pack()
        self.label = tk.Label(master=self.frame, text=text, width=12)
        self.label.pack(side="left")
        self.spinbox = tk.Spinbox(master=self.frame)
        self.spinbox["increment"] = increment
        self.spinbox["textvariable"] = textvariable
        self.spinbox["from"] = _from
        self.spinbox["to"] = _to
        self.spinbox["width"] = digit + 1
        self.spinbox.pack(side="left")
        self.scale = tk.Scale(master=self.frame, orient="horizontal")
        self.scale["length"] = 200
        self.scale["sliderlength"] = 15
        self.scale["digits"] = 1
        self.scale["resolution"] = increment
        self.scale["variable"] = textvariable
        self.scale["from"] = _from
        self.scale["to"] = _to
        self.scale["showvalue"] = False
        self.scale.pack(side="left")

