# -*- coding: utf-8 -*-

from .constants import PLANETS
from .modules import os, dt, tz, swe, timezone, TimezoneFinder
from .conversions import convert_degree, reverse_convert_degree, dd_to_dms

swe.set_ephe_path(os.path.join(os.getcwd(), "Eph"))


class Zodiac:
    def __init__(
            self,
            year: int = 0,
            month: int = 0,
            day: int = 0,
            hour: int = 0,
            minute: int = 0,
            second: int = 0,
            lat: float = .0,
            lon: float = .0,
            hsys: str = "",
    ):
        self.LOCAL_YEAR = year
        self.LOCAL_MONTH = month
        self.LOCAL_DAY = day
        self.LOCAL_HOUR = hour
        self.LOCAL_MINUTE = minute
        self.LOCAL_SECOND = second
        self.LAT = lat
        self.LON = lon
        self.HSYS = hsys
        self.UTC_YEAR = self.local_to_utc()["year"]
        self.UTC_MONTH = self.local_to_utc()["month"]
        self.UTC_DAY = self.local_to_utc()["day"]
        self.UTC_HOUR = self.local_to_utc()["hour"]
        self.UTC_MINUTE = self.local_to_utc()["minute"]
        self.UTC_SECOND = self.local_to_utc()["second"]
        self.JD = self.julday()

    def julday(self):
        t_given = dt.strptime(
            f"{str(self.UTC_YEAR).zfill(4)}.{self.UTC_MONTH}.{self.UTC_DAY}",
            "%Y.%m.%d"
        )
        t_limit = dt.strptime("1582.10.15", "%Y.%m.%d")
        if (t_limit - t_given).days > 0:
            calendar = swe.JUL_CAL
        else:
            calendar = swe.GREG_CAL
        jd = swe.julday(
            self.UTC_YEAR,
            self.UTC_MONTH,
            self.UTC_DAY,
            self.UTC_HOUR
            + (self.UTC_MINUTE / 60)
            + (self.UTC_SECOND / 3600),
            calendar
        )
        deltat = swe.deltat(jd)
        return round(jd + deltat, 6)

    def local_to_utc(self):
        local_zone = tz.gettz(
            str(
                timezone(
                    TimezoneFinder().timezone_at(
                        lat=self.LAT, lng=self.LON
                    )
                )
            )
        )
        utc_zone = tz.gettz("UTC")
        global_time = dt.strptime(
            f"{str(self.LOCAL_YEAR).zfill(4)}-"
            f"{self.LOCAL_MONTH}-{self.LOCAL_DAY} "
            f"{self.LOCAL_HOUR}:{self.LOCAL_MINUTE}:{self.LOCAL_SECOND}",
            "%Y-%m-%d %H:%M:%S"
        )
        local_time = global_time.replace(tzinfo=local_zone)
        utc_time = local_time.astimezone(utc_zone)
        return {
            "year": utc_time.year,
            "month": utc_time.month,
            "day": utc_time.day,
            "hour": utc_time.hour,
            "minute": utc_time.minute,
            "second": utc_time.second
        }

    def planet_pos(self, planet: int = 0):
        calc = convert_degree(
            degree=swe.calc(self.JD, planet)[0]
        )
        return calc[1], reverse_convert_degree(calc[0], calc[1])

    def patterns(self, planet: str = ""):
        info = [planet]
        planet = self.planet_pos(planet=PLANETS[planet]["number"])
        info.extend([*convert_degree(planet[1])][::-1])
        info[-1] = dd_to_dms(info[-1])
        return info

