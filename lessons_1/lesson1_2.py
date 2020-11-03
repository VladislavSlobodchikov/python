import time


# tm =float(input("Enter time value in seconds :  ")

str = 2228
hour = int(str/3600)
min = int((str - (hour*3600))/60)
sec = int(str - (hour*3600) - (min*60))

print('%02d:%02d:%02d'% (hour,min,sec))
print("{0:2}:{1:2}:{2:2}".format(hour,min,sec))