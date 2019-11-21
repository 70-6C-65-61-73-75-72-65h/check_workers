# from myapp.models import Simulation, get_simulation

# from datetime import timedelta, date
# import time
# def daterange(start_date, end_date):
#     for n in range(int ((end_date - start_date).days)):
#         yield start_date + timedelta(n)

# start_date = date(2013, 1, 1)
# end_date = date(2015, 6, 2)
# for single_date in daterange(start_date, end_date):
#     print(single_date.strftime("%Y-%m-%d"))


# Show the last n days from today:

# import datetime
# for i in range(0, 100):
#     print((datetime.date.today() + datetime.timedelta(i)).isoformat())
# Output:

# 2016-06-29
# 2016-06-30
# 2016-07-01
# 2016-07-02
# 2016-07-03
# 2016-07-04

# import numpy as np
# from datetime import datetime, timedelta
# d0 = datetime(2009, 1,1)
# d1 = datetime(2010, 1,1)
# dt = timedelta(days = 1)
# dates = np.arange(d0, d1, dt).astype(datetime)
# The use of astype is to convert from numpy.datetime64 to an array of datetime.datetime objects.

# def simulate_days():
#     sim = get_simulation()
#     sim.today = sim.today + timedelta(1)
#     time.sleep(1)
#     sim.save()

# def main():
#     add_days()

# main()
# status = False
# status = True if status == False else False
# print(status)