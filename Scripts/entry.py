# -*- coding: utf-8 -*-

from .modules import tk


class Entry(tk.Entry):
    def __init__(self, limit: int = 0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack()
        self.bind(
            sequence="<KeyRelease>",
            func=lambda event: self.max_char(limit=limit)
        )

    def max_char(self, limit: int = 0):
        if len(self.get()) > limit:
            self.delete(str(limit))


class EntryFrame(tk.Frame):
    def __init__(
            self,
            text: str = "",
            side: str = "",
            limit: int = 0,
            width: int = 0,
            *args,
            **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.pack(side=side)
        self.label = tk.Label(master=self, text=text).pack()
        self.entry = Entry(master=self, limit=limit, width=width,)


class EntryField(tk.Frame):
    def __init__(
            self,
            text: str = "",
            side: str = "",
            dictionaries: tuple = (),
            *args,
            **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.configure(bd=1, relief="sunken")
        self.pack(side=side)
        self.dictionaries = dictionaries
        self.label = tk.Label(
            master=self, text=text.center(13, " "),
            font="Default 12 bold"
        )
        self.label.pack(side="top")
        self.entries = self.create_fields()

    def create_fields(self):
        fields = {}
        for i in self.dictionaries:
            frame = tk.Frame(master=self)
            frame.pack()
            for k, v in i.items():
                fields[k] = EntryFrame(
                    master=frame,
                    limit=v["limit"],
                    text=k,
                    width=v["limit"],
                    side="left",
                ).entry
        return fields

