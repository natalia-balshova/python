import datetime

seconds = int(input('Введите время в секундах'))
hour = seconds // 3600
min = (seconds - hour * 3600) // 60
sec = (seconds - hour * 3600 - min * 60)
print(datetime.time(hour, min, sec))