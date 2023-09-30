from datetime import datetime,  timedelta


now = datetime.now()


current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
result = now + timedelta(minutes=330) 
print("India Current Time =", result)