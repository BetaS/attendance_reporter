import datetime
from src.user_db import UserModel

from typing import NamedTuple


class TimeModel(NamedTuple):
    start_time: datetime.datetime
    end_time: datetime.datetime


def load_times(users, sheet, year, month):
    user_id = None
    state = 0  # 1 - 날짜인식, 2 - 시간인식
    for row in range(4, sheet.nrows):
        data = sheet.row(row)
        if data[1].value == "사용자번호:":
            state = 1
            user_id = int(data[4].value)
            continue
        if state == 1:
            state = 2
            continue
        if state == 2:
            print(data)
            for col in range(1, len(data)):
                times = users[user_id].times
                if col not in times:
                    times[col] = TimeModel(start_time=None, end_time=None)

                model = times[col]
                times = data[col].value.split("\n")
                for time in times:
                    time = time.split(":")
                    if len(time) == 2:
                        t = datetime.time(hour=int(time[0]), minute=int(time[1]))

                        if t < datetime.time(hour=6):
                            times[col-1].end_time = t

                        if model.start_time:
                            model.start_time = t

    return users