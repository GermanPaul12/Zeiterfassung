import pandas as pd
import numpy as np
import datetime as dt


def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + dt.timedelta(n)





def write_to_csv():
    pass


dates = [dtt.strftime('%Y-%m-%d') for dtt in daterange(dt.datetime.strptime(f"{dt.datetime.now().year-2}-01-01", "%Y-%m-%d"),
                                                                                             dt.datetime.strptime("2025-09-30", "%Y-%m-%d"))]
