import gspread
from oauth2client.service_account import ServiceAccountCredentials

SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
CREDS_FILE = "your-google-credentials.json"

def get_sheet(sheet_url, worksheet_index=0):
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_FILE, SCOPE)
    client = gspread.authorize(creds)
    sheet = client.open_by_url(sheet_url).get_worksheet(worksheet_index)
    return sheet

def get_customer_info(name):
    sheet = get_sheet("https://docs.google.com/spreadsheets/d/1Qnn9Bk3Y0kRMVIQyNYjVeBstw4MbiOfGY09PzIN3FNE/edit")
    records = sheet.get_all_records()
    for row in records:
        if name.lower() in row["Account Name"].lower():
            return row
    return {}

def get_product_price(item):
    sheet = get_sheet("https://docs.google.com/spreadsheets/d/1081CU00TAxYuvVdniDLFOu5ZZ8WJwGW0taMb6cPnsq8/edit")
    records = sheet.get_all_records()
    for row in records:
        if item.lower() in row["Product"].lower():
            return float(row["Price"])
    return 0.0
