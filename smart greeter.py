import time 
h = int(time.strftime('%H')) 
if (h >= 6 and h < 12) :
    print("Good Morning Sir")
elif (h >= 12 and h < 17) :
    print(f"Good Afternoon Sir")
elif (h >= 17 and h < 23) :
    print(f"Good Evening Sir")
else :
    print(f"Good Night Sir")