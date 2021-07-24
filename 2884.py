hours,minutes=input().split()
hours=int(hours)
minutes=int(minutes)

minutes-=45
if minutes<0:
    if hours-1<0:
        hours+=24
    print(hours-1,minutes+60)

else:
    print(hours,minutes)