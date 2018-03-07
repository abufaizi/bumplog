import datetime

start_date = datetime.date.today()

date_1 = datetime.datetime.strptime(start_date, "%m/%d/%y")

end_date = date_1 + datetime.timedelta(days=10)

print(date_1 + ', ' + end_date)
