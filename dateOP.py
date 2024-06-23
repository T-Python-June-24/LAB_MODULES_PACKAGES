import datetime

def current_date():
    today = datetime.datetime.today()
    print(today.strftime("%x"))