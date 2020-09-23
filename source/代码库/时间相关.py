'''
判断某一天是日历中的第几天

例如：2020.08.31是日历中的第1天
2020.09.23是日历中的第24天

思路：
设置一个初始时间（1969-12-28），返回当前时间是周几，本月1号是周几
'''
import datetime
# 19700101-4

date_input = '2020-09-23'
date_of_week = datetime.datetime.strptime(date_input,'%Y-%m-%d').weekday()
fstd_of_week = datetime.datetime.strptime(date_input[0:7]+'-01','%Y-%m-%d').weekday()
print(fstd_of_week-1+datetime.datetime.strptime(date_input,'%Y-%m-%d').day)