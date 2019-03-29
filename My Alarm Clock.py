# 3/28/2019 - still need some tweaking

# // countdown feature //

import playsound # a little tool that plays .mp3 file
import sys # help with time countdown
import time # help with time countdown
import datetime

xx = str(input('Pick a format ( [1] Seconds or [2] Minutes):   '))  # user picks a time
x: int = int(input('Pick a time (a number):   '))  # user picks a time


if '1' == xx:
    print('Seconds until Countdown Finishes: ')
    y = x*1
elif '2' == xx:
    print('Seconds until Countdown Finishes: ')
    y = x*60

for num in range(int(y),0,-1):
    sys.stdout.write(str(num)+' more seconds')
    #sys.stdout.flush()
    time.sleep(1)
    print(' ' + str(datetime.datetime.now()))
playsound.playsound(("C:\\Users\\Daniel & AnAn\\Downloads\\starcraft_t_no_enrgy.mp3" ), True)

#now = datetime.datetime.now()
#future_time = now + datetime.timedelta(minutes = x)
#print(future_time)


# /// Alarm Clock ///

import playsound
import sys
import time
import datetime

x: int = int(input('Pick a time (a number):   '))
xx = str(input('Pick a format ( Seconds or Minutes):   '))

if 'Seconds'.lower() or 'Seconds'.upper() == xx:
    print('Seconds until Countdown Finishes: ')
    y = x*1
elif 'Minutes'.lower() or 'Seconds'.upper() == xx:
    print('Seconds until Countdown Finishes: ')
    y = x*60

for num in range(0,int(y),1):
    sys.stdout.write(str(num+1)+' seconds has gone by...')
    print(' ' + str(datetime.datetime.now()))
    time.sleep(1)


playsound.playsound(("C:\\Users\\Daniel & AnAn\\Downloads\\starcraft_t_no_enrgy.mp3" ), True)

now = datetime.datetime.now()
future_time = now + datetime.timedelta(minutes = x)
print(future_time)

