import datetime

date = datetime.datetime.now()
hour = int(date.strftime("%H"))

message = "Good "
name = input("What is your name? ")
if hour < 12:
    message += "morning"
elif hour < 16:
    message += "afternoon"
elif hour < 18:
    message += "evening"
else:
    message += "night"

print(f"Hello {name}, {message}")
