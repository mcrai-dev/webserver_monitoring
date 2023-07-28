# function to make countdown
from flask import jsonify
import time
import datetime as dt


# def countdown(stop):
#     while True:
#         difference = stop - dt.datetime.now()
#         count_hours, rem = divmod(difference.seconds, 3600)
#         count_minutes, count_seconds = divmod(rem, 60)
#         if difference.days == 0 and count_hours == 0 and count_minutes == 0 and count_seconds == 0:
#             print("time is up!")
#             break
#         print('the count is: ' + str(difference.days) + " D, " + str(count_hours) +
#               " H:" + str(count_minutes) + " M:" + str(count_seconds) + " S")
#         text = str(difference.days) + " D, " + str(
#             count_hours) + " H:" + str(count_minutes) + " M:" + str(count_seconds) + " S"
#         time.sleep(1)


def chooseDate(yyyy, MM, dd, hh, min, ss):
    tab = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
           "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    end_time = dt.datetime(int(yyyy), int(
        tab.index(MM)) + 1, int(dd), int(hh), int(min), int(ss))
    #print(f"index choosen is{int(tab.index(MM)) +1}")
    #print(f'YYYY= {yyyy} month = {int(tab.index(MM)) +1} day = {dd} hour={hh} min = {min} sec = {ss}')
    return end_time
