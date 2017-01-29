import datetime
import os
import time
import winsound

def notice(msg):
    winsound.PlaySound("ALARM1", winsound.SND_ASYNC)
    os.popen("wscript.exe speak.vbs "+msg)

def getTimeStamp(timeStr):
    timeArray = time.strptime(timeStr, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    return timeStamp

def getTimeStr():
    now = datetime.datetime.now()
    dayTime = now.strftime("%Y-%m-%d")
    print(dayTime)
    return dayTime


class TimeList():

    def __init__(self, fileName="timeList.txt"):
        f = open(fileName, "r", encoding="utf-8")
        data = f.readlines()
        f.close()
        times = {}
        daytime = getTimeStr()
        ttTime = int(time.time())
        for line in data:
            line = line.strip()
            cr = line.split(",")
            tTime = {}
            tTime["time"] = cr[1].strip()
            tTime["msg"] = cr[0].strip()
            tTime["ctime"] = getTimeStamp(daytime+" "+tTime["time"])
            if tTime["ctime"] < ttTime:
                tTime["ctime"] = tTime["ctime"]+86400
            times[tTime["time"]] = tTime
            print(tTime["ctime"])

        self.times = times

    def tick(self):
        tTime = int(time.time())
        print("tTime:"+str(tTime))
        for timest in self.times:
            cTime = self.times[timest]
            if int(cTime["ctime"]) <= tTime:
                cTime["ctime"] = int(cTime["ctime"])+86400
                print("next:"+str(cTime["ctime"]))
                notice(cTime["msg"])

def mainLoop():
    tT = TimeList()
    while(1):
        tT.tick()
        time.sleep(10)

if __name__ == "__main__":
    mainLoop()
