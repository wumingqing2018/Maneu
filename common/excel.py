from openpyxl import load_workbook
import json


def execl_to_json(execl):
    try:
        wb = load_workbook(execl, data_only=True)
        json_sheet = {}
        for sheet in wb.sheetnames:
            ws = wb[sheet]
            json_row = {}
            for r in range(5, 48):
                json_col = []
                for c in range(1, 21):
                    json_col.append(ws.cell(r, c).value)
                json_row[ws.cell(r, 1).value] = json_col
            json_sheet[sheet] = json_row
        return json.dumps(json_sheet)
    except BaseException as msg:
        print(msg)
        return None
