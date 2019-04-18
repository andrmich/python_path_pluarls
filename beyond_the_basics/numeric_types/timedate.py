import datetime

a = datetime.datetime(year=2014, month=5, day=8, hour=14, minute=22)
b = datetime.datetime(year=2014, month=3, day=8, hour=12, minute=9)

d = a - b
seconds = d.total_seconds()

in_three_weeks = datetime.date.today() + datetime.timedelta(weeks=1) * 3

cet = datetime.timezone(datetime.timedelta(hours=1), 'CET')
departure = datetime.datetime(year=2014, month=1, day=7, hour=11, minute=30, tzinfo=cet)
arrival = datetime.datetime(year=2014, month=1, day=7, hour=13, minute=5, tzinfo=datetime.timezone.utc)
flight_duration = arrival - departure

if __name__ == '__main__':
    print(d)
    print(seconds)
    print(in_three_weeks)
    print(flight_duration)
