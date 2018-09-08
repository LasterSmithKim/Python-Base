import calendar

'''
日历模块


'''


#返回指定某年某月的月历
print(calendar.month(2017,7))

#返回指定某年的日历
print(calendar.calendar(2017))

#闰年返回True，否则返回False
print(calendar.isleap(2020))

#返回某个月的weekday的第一天和这个月所有的天数
print(calendar.monthrange(2017,9))

#返回某个月以每一周为元素的列表
print(calendar.monthcalendar(2017,7))



