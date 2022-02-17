def sleep():
   XX = int(input("Sleep time(minutes): "))
   HH = int(input("Hours : "))
   MM = int(input("Minutes : "))
   if 5 < HH < 0:
       print("Wrong time! Katya go to sleep after midnight")
       return
   #if 0 > HH > 24:
    #   print("Wrong time format!")
     #  return
   start_time = HH * 60 + MM
   wakeup_time = start_time + XX
   clock_time_H = int(wakeup_time / 60)
   clock_time_M = wakeup_time % 60
   if clock_time_H >= 24 and clock_time_M > 0:
       print("Next day")
       return
   print("Wake up at ", clock_time_H, "hours and")
   print(clock_time_M, "minutes")
sleep()



