import func_module

# func_module.moodule_show()

nowdate = func_module.datetime.datetime.now()
# print(nowdate)

x_mas = nowdate.replace(month = 12, day = 25)

now_year = x_mas.year
now_month = x_mas.month
now_day = x_mas.day


print('{}년 {}월 {}일'.format(now_year, now_month, now_day))
