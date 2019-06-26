from datetime import datetime
now = datetime.now()
print (now.month - 1)
print (now.year)
if now.month < 10:
    mesEAno = (str(now.year) + '0' + str(now.month))
else:
    mesEAno = (str(now.year) + str(now.month))
print(mesEAno)
