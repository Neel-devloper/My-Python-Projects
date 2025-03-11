# date difference teller

print('THEY HAVE TO BE IN THE SAME YEAR!')
print('MM/DD')
date1 = input('enter first date: ')
date2 = input('enter second date: ')

date1_day = int(date1.split('/')[1])
date1_month = int(date1.split('/')[0])

date2_day = int(date2.split('/')[1])
date2_month = int(date2.split('/')[0])

jan = 0
feb = 31
mar = 59
apr = 90
may = 120
jun = 151
jul = 181
aug = 212
sep = 243
oct = 273
nov = 304
dec = 334

if date1_month == 1:
    days_done1 = jan + date1_day
if date1_month == 2:
    days_done1 = feb + date1_day
if date1_month == 3:
    days_done1 = mar + date1_day
if date1_month == 4:
    days_done1 = apr + date1_day
if date1_month == 5:
    days_done1 = may + date1_day
if date1_month == 6:
    days_done1 = jun + date1_day
if date1_month == 7:
    days_done1 = jul + date1_day
if date1_month == 8:
    days_done1 = aug + date1_day
if date1_month == 9:
    days_done1 = sep + date1_day
if date1_month == 10:
    days_done1 = oct + date1_day
if date1_month == 11:
    days_done1 = nov + date1_day
if date1_month == 12:
    days_done1 = dec + date1_day

if date2_month == 1:
    days_done2 = jan + date2_day
if date2_month == 2:
    days_done2 = feb + date2_day
if date2_month == 3:
    days_done2 = mar + date2_day
if date2_month == 4:
    days_done2 = apr + date2_day
if date2_month == 5:
    days_done2 = may + date2_day
if date2_month == 6:
    days_done2 = jun + date2_day
if date2_month == 7:
    days_done2 = jul + date2_day
if date2_month == 8:
    days_done2 = aug + date2_day
if date2_month == 9:
    days_done2 = sep + date2_day
if date2_month == 10:
    days_done2 = oct + date2_day
if date2_month == 11:
    days_done2 = nov + date2_day
if date2_month == 12:
    days_done2 = dec + date2_day

if int(days_done2) - int(days_done1) < 0:
    print('date1 is older than date2')
else:
    print(f'the difference between {date1} and {date2} is {abs(days_done1 - days_done2)} days')
