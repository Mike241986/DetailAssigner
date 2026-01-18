import csv
import calendar


def create_calendar(year, month, detail):
    m = ['','January','February','March','April','May','June','July','August','September','October','November','December']
    cal = calendar.monthcalendar(int(year), int(month))
    headers = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

    with open(f'{detail}_{m[int(month)]}_{year}.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for week in cal:
            writer.writerow([day if day != 0 else '   ' for day in week])




