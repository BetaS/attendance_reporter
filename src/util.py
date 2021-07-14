import xlrd


def open_sheet(path: str):
    wb = xlrd.open_workbook(path)
    return wb.sheet_by_index(0)


if __name__ == "__main__":
    open_sheet("../data/2021 06/근무기록보고서.xls")
