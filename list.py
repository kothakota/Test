from datetime import datetime

b= datetime.now()

print(b)

a = int(input("Enter Day Number"))
weekday = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

if a>6 or a<0:
    print("Please Enter a Valid Date")
else:
    print(weekday[a])