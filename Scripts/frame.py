# -*- coding: utf-8 -*-

from .zodiac import Zodiac
from .label import LabelField
from .entry import EntryField
from .treeview import Treeview
from .optionmenu import OptionFrame
from .spinboxscale import SpinboxScale
from .constants import PLANETS, SIGNS, DATE, TIME, DMS, COORDINATE
from .modules import (
    tk, dt, td, Pbar, time, timezone, showinfo, TimezoneFinder, Thread
)


class Frame(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack()
        self.active = False
        self.configure(height=2000)
        self.mainframes = self.create_frames(
            master=self,
            n=2,
            side="left",
        )
        self.left_frame = next(self.mainframes)
        self.right_frame = next(self.mainframes)
        self.subframes = self.create_frames(
            master=self.left_frame,
            n=7,
            side="top"
        )
        self.coordinates_frame = next(self.subframes)
        self.date_frame = next(self.subframes)
        self.optionmenu_frame = next(self.subframes)
        self.position_frame = next(self.subframes)
        self.spinboxscale_frame = next(self.subframes)
        self.current_frame = next(self.subframes)
        self.button_frame = next(self.subframes)
        self.var = self.doublevar(0, 86400 * 30, 0, 1)
        self.coordinates = EntryField(
            master=self.coordinates_frame,
            text="Coordinates",
            side="top",
            dictionaries=(COORDINATE,)
        )
        self.starting_date = EntryField(
            master=self.date_frame,
            text="Starting Date",
            side="left",
            dictionaries=(DATE, TIME)
        )
        self.ending_date = EntryField(
            master=self.date_frame,
            text="Ending Date",
            side="left",
            dictionaries=(DATE, TIME)
        )
        self.current_labels = LabelField(
            master=self.current_frame,
            texts=("Sign", "Position", "Date"),
            title="Current"
        )
        self.planet = OptionFrame(
            master=self.optionmenu_frame,
            values=PLANETS,
            text="Planet",
            side="left"
        )
        self.sign = OptionFrame(
            master=self.optionmenu_frame,
            values=SIGNS,
            text="Sign",
            side="left"
        )
        self.position = EntryField(
            master=self.position_frame,
            text="Position",
            side="left",
            dictionaries=(DMS,)
        )
        self.spinboxscale = SpinboxScale(
            master=self.spinboxscale_frame,
            textvariable=self.var[0],
            increment=self.var[3].get(),
            _from=self.var[2].get(),
            _to=self.var[1].get(),
            digit=6,
            text="Seconds",
            title="Time Increase Amount"
        )
        self.start_button = tk.Button(
            master=self.button_frame,
            text="Start",
            command=lambda: Thread(target=self.start).start()
        )
        self.start_button.pack(side="left")
        self.stop_button = tk.Button(
            master=self.button_frame,
            text="Stop",
            command=self.stop
        )
        self.stop_button.pack(side="left")
        self.treeview = Treeview(master=self.right_frame)

    @staticmethod
    def create_frames(master=None, n: int = 0, side: str = ""):
        for i in range(n):
            frame = tk.Frame(master=master)
            frame.pack(side=side, fill=tk.Y)
            yield frame

    @staticmethod
    def doublevar(*args):
        return [tk.DoubleVar(value=i) for i in args]

    def stop(self):
        self.active = False

    def start(self):
        self.active = True
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        lat = self.coordinates.entries["Latitude"].get()
        lon = self.coordinates.entries["Longitude"].get()
        try:
            lat = float(lat)
        except ValueError:
            showinfo(
                title="Info",
                message="Invalid latitude value."
            )
            return
        try:
            lon = float(lon)
        except ValueError:
            showinfo(
                title="Info",
                message="Invalid longitude value."
            )
            return
        try:
            timezone(
                TimezoneFinder().timezone_at(
                    lat=lat, lng=lon
                )
            )
        except AttributeError:
            showinfo(
                title="Info",
                message="Invalid timezone for given "
                        "latitude and longitude values."
            )
            return
        s_year = self.starting_date.entries["Year"].get()
        s_month = self.starting_date.entries["Month"].get()
        s_day = self.starting_date.entries["Day"].get()
        s_hour = self.starting_date.entries["Hour"].get()
        s_minute = self.starting_date.entries["Minute"].get()
        s_second = self.starting_date.entries["Second"].get()
        try:
            start = dt.strptime(
                f"{s_year}.{s_month}.{s_day} "
                f"{s_hour}:{s_minute}:{s_second}",
                "%Y.%m.%d %H:%M:%S"
            )
        except ValueError:
            showinfo(
                title="Info",
                message="Invalid date for starting time."
            )
            return
        e_year = self.ending_date.entries["Year"].get()
        e_month = self.ending_date.entries["Month"].get()
        e_day = self.ending_date.entries["Day"].get()
        e_hour = self.ending_date.entries["Hour"].get()
        e_minute = self.ending_date.entries["Minute"].get()
        e_second = self.ending_date.entries["Second"].get()
        try:
            end = dt.strptime(
                f"{e_year}.{e_month}.{e_day} "
                f"{e_hour}:{e_minute}:{e_second}",
                "%Y.%m.%d %H:%M:%S"
            )
        except ValueError:
            showinfo(
                title="Info",
                message="Invalid date for starting time."
            )
            return
        if start >= end:
            showinfo(
                title="Info",
                message="Start date can't be equal or greater to end date."
            )
            return
        planet = self.planet.optionmenu.var.get()
        if not planet:
            showinfo(
                title="Info",
                message="Planet field can't be remained empty."
            )
            return
        sign = self.sign.optionmenu.var.get()
        degree = self.position.entries["Degree"].get()
        try:
            degree = int(degree)
            if degree > 29:
                showinfo(
                    title="Info",
                    message="Degree must be between 0\u00b0-29\u00b0."
                )
                return
        except ValueError:
            showinfo(
                title="Info",
                message="Invalid value for degree."
            )
            return
        minute = self.position.entries["Minute"].get()
        if minute != "":
            try:
                minute = int(minute)
                if minute > 59:
                    showinfo(
                        title="Info",
                        message="Minute must be between 0\u00b0-59\u00b0."
                    )
                    return
            except ValueError:
                showinfo(
                    title="Info",
                    message="Invalid value for minute."
                )
                return
        second = self.position.entries["Second"].get()
        if second != "":
            try:
                second = int(second)
                if second > 59:
                    showinfo(
                        title="Info",
                        message="Second must be between 0\u00b0-59\u00b0."
                    )
                    return
            except ValueError:
                showinfo(
                    title="Info",
                    message="Invalid value for second."
                )
                return
        if not self.spinboxscale.scale.get():
            showinfo(
                title="Info",
                message="Time increase amount shouldn't "
                        "be 0 at first run."
            )
            return
        if minute != "" and second == "":
            dms = f"{degree}\u00b0{minute}'"
        elif second != "" and minute == "":
            dms = f'{degree}\u00b0{second}"'
        elif minute == "" and second == "":
            dms = f'{degree}\u00b0'
        else:
            dms = f'''{degree}\u00b0{minute}\'{second}"'''
        index = 0
        size = int((end - start).total_seconds())
        count = 0
        now = time()
        pframe = tk.Frame(master=self.left_frame)
        pbar = Pbar(
            master=pframe,
            orient="horizontal",
            length=200,
            mode="determinate"
        )
        pstring = tk.StringVar()
        plabel = tk.Label(
            master=pframe,
            textvariable=pstring
        )
        pframe.pack()
        pbar.pack()
        plabel.pack()
        while start < end:
            if not self.active:
                break
            scale = int(self.spinboxscale.scale.get())
            count += scale
            pbar["value"] = count
            pbar["maximum"] = size
            pstring.set(self.progress_info(c=count, s=size, n=now))
            pattern = Zodiac(
                year=start.year,
                month=start.month,
                day=start.day,
                hour=start.hour,
                minute=start.minute,
                second=start.second,
                lat=lat,
                lon=lon,
                hsys="P"
            ).patterns(planet=planet)
            if minute != "" and second == "":
                pattern[2] = pattern[2].split("'")[0] + "'"
            elif second != "" and minute == "":
                pattern[2] = pattern[2].split("\u00b0")[0] + \
                             "\u00b0" + \
                             pattern[2].split("'")[1]
            elif minute == "" and second == "":
                pattern[2] = pattern[2].split("\u00b0")[0] + \
                             "\u00b0"
            start += td(seconds=scale)
            self.current_labels.sign.var.set(pattern[1])
            self.current_labels.position.var.set(pattern[2])
            self.current_labels.date.var.set(
                start.strftime("%Y.%m.%d %H:%M:%S")
            )
            if sign:
                if pattern[1] == sign:
                    if dms == pattern[2]:
                        self.treeview.insert(
                            parent="",
                            index=index,
                            values=[
                                *pattern,
                                start.strftime("%Y.%m.%d %H:%M:%S")
                            ]
                        )
                        index += 1
            else:
                if dms == pattern[2]:
                    self.treeview.insert(
                        parent="",
                        index=index,
                        values=[
                            *pattern,
                            start.strftime("%Y.%m.%d %H:%M:%S")
                        ]
                    )
                    index += 1
            self.update()
        self.current_labels.sign.var.set("None")
        self.current_labels.position.var.set("None")
        self.current_labels.date.var.set("None")
        pframe.destroy()

    @staticmethod
    def progress_info(c: int = 0, s: int = 0, n: float = .0):
        return \
            f"{int(100 * c / s)} %, " \
            f"{int(c / (time() - n))} c/s, " \
            f"{int(s / (c / (time() - n))) - int(time() - n)}" \
            f" seconds remaining."

