from src import util, user_db, time_db, drive


if __name__ == "__main__":
    sh = util.open_sheet("data/사용자정보.xls")
    users = user_db.load_user_model(sh)

    sh = util.open_sheet("data/2021 06/근무기록보고서.xls")
    result = time_db.load_times(users, sh, year=2021, month=6)
    print(result[1])
    for k, v in result.items():
        drive.make_data("./out", 2021, 6, v)