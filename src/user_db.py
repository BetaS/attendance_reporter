from typing import NamedTuple


class UserModel(NamedTuple):
    idx: int
    name: str
    dept: str
    times: dict


def load_user_model(sheet):
    result = {}
    row = 10

    while row < sheet.nrows:
        data = sheet.row(row)
        if not data[0]:
            break

        result[int(data[0].value)] = UserModel(idx=int(data[0].value), name=data[1].value, dept=data[2].value, times={})
        row += 1

    return result
