import datetime
from src.user_db import UserModel


class TimeModel:
    start_time: datetime.datetime
    end_time: datetime.datetime

    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"{self.start_time} ~ {self.end_time}"


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
            for col in range(1, len(data)):
                times = users[user_id].times
                if col not in times:
                    # times[col] = TimeModel(start_time=None, end_time=None)
                    times[col] = []

                lines = data[col].value.split("\n")
                for line in lines:
                    t = line.split(":")
                    if len(t) == 2:
                        t2 = datetime.time(hour=int(t[0]), minute=int(t[1]))
                        times[col].append(t2)

                        # if t2 < datetime.time(hour=6):
                        #     times[col-1].end_time = t2
                        # elif times[col].start_time is not None:
                        #     times[col].end_time = t2
                        # elif times[col].start_time is None:
                        #     times[col].start_time = t2

    return users