# -*- coding: utf-8 -*-

import os
import sys
import tkinter as tk
import swisseph as swe

from time import time
from dateutil import tz
from pytz import timezone
from threading import Thread
from tkinter.messagebox import showinfo
from tkinter.ttk import Treeview as Tv
from timezonefinder import TimezoneFinder
from tkinter.ttk import Progressbar as Pbar
from datetime import (datetime as dt, timedelta as td)

