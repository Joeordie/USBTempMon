import os
import threading
import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)

temps = []

def maths(temp):
    temps.append(temp)
    #do averaging
    average = 0
    for i in range(len(temps)):
        average = average + temps[i]
    average = average / temps.__len__()

    if temps.__len__() >= 60:
        strtemp = str(temp)
        straverage = str(average)
        messaging(strtemp, straverage)

def messaging(temp, average):
    message = ('telegram-cli -W -e "msg Jonathan_Carroll the current temp is ' + temp +
        ' the average is ' + average + '."')
    os.system(message)
    temps[:] = []

def overHeatMsg(temp):
    message = message = ('telegram-cli -W -e "msg Jonathan_Carroll WARNING the current temp is ' + temp +
        '."')
    os.system(message)
    # sleeping for 300 secs is 5 minutes
    threading._sleep(300)

while 1 == 1:
    # read off the USB device
    line = ser.readline()
    print(line)
    intLine = int(line)
    if (intLine > 100):
        strLine = str(intLine)
        overHeatMsg(strLine)

    maths(intLine)





