from dateutil.relativedelta import relativedelta
import time, datetime as dt
start_time = time.time()

sundays = 0
date = dt.date(1901,1,1)
while date <= dt.date(2000,12,31):
	if date.weekday() == 6:
		sundays += 1
	date += relativedelta(months=1)

print()
print('there were '+ str(sundays) +' sundays in the 20th century')
print('runtime: %s sec' % (time.time() - start_time))
print()
