from src import util, user_db, time_db


if __name__ == "__main__":
    sh = util.open_sheet("data/사용자정보.xls")
    users = user_db.load_user_model(sh)

    sh = util.open_sheet("data/2021 06/근무기록보고서.xls")
    result = time_db.load_times(users, sh, year=2021, month=6)

    print(result)