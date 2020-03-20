# -*- coding: utf-8 -*-

from .modules import swe

SIGNS = {
    "Aries": {
        "symbol": "\u2648",
        "color": "#FF0000"
    },
    "Taurus": {
        "symbol": "\u2649",
        "color": "#00FF00"
    },
    "Gemini": {
        "symbol": "\u264A",
        "color": "#FFFF00"
    },
    "Cancer": {
        "symbol": "\u264B",
        "color": "#0000FF"
    },
    "Leo": {
        "symbol": "\u264C",
        "color": "#FF0000"
    },
    "Virgo": {
        "symbol": "\u264D",
        "color": "#00FF00"
    },
    "Libra": {
        "symbol": "\u264E",
        "color": "#FFFF00"
    },
    "Scorpio": {
        "symbol": "\u264F",
        "color": "#0000FF"
    },
    "Sagittarius": {
        "symbol": "\u2650",
        "color": "#FF0000"
    },
    "Capricorn": {
        "symbol": "\u2651",
        "color": "#00FF00"
    },
    "Aquarius": {
        "symbol": "\u2652",
        "color": "#FFFF00"
    },
    "Pisces": {
        "symbol": "\u2653",
        "color": "#0000FF"
    }
}

PLANETS = {
    "Sun": {
        "number": swe.SUN,
        "symbol": "\u2299"
    },
    "Moon": {
        "number": swe.MOON,
        "symbol": "\u263E"
    },
    "Mercury": {
        "number": swe.MERCURY,
        "symbol": "\u263F"
    },
    "Venus": {
        "number": swe.VENUS,
        "symbol": "\u2640"
    },
    "Mars": {
        "number": swe.MARS,
        "symbol": "\u2642"
    },
    "Jupiter": {
        "number": swe.JUPITER,
        "symbol": "\u2643"
    },
    "Saturn": {
        "number": swe.SATURN,
        "symbol": "\u2644"
    },
    "Uranus": {
        "number": swe.URANUS,
        "symbol": "\u2645"
    },
    "Neptune": {
        "number": swe.NEPTUNE,
        "symbol": "\u2646"
    },
    "Pluto": {
        "number": swe.PLUTO,
        "symbol": "\u2647"
    },
    "True": {
        "number": swe.TRUE_NODE,
        "symbol": "\u260A"
    }
}

COORDINATE = {
    "Latitude": {"limit": 10},
    "Longitude": {"limit": 10}
}

DATE = {
    "Year": {"limit": 4},
    "Month": {"limit": 2},
    "Day": {"limit": 2}
}

TIME = {
    "Hour": {"limit": 2},
    "Minute": {"limit": 2},
    "Second": {"limit": 2}
}

DMS = {
    "Degree": {"limit": 2},
    "Minute": {"limit": 2},
    "Second": {"limit": 2}
}

