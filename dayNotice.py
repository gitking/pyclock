import winsound
import os
import time
import datetime

dayTimeS=24*60*60;


def notice(msg="警告"):
    winsound.PlaySound('ALARM1', winsound.SND_ASYNC)
    os.popen('wscript.exe speak.vbs '+msg)

def adptStr(tstr,data):
    for kk in data:
        tstr=tstr.replace(kk,data[kk])
    return tstr

def getTimeStamp(timeStr):
    timeArray = time.strptime(timeStr, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    return timeStamp

def getTimeStr():
    now=datetime.datetime.now()
    dayTime=now.strftime("%Y-%m-%d")
    print(dayTime)
    return dayTime


class TimeList:

    def __init__(self,fileName="timeList.txt"):
        global dayTimeS
        f=open(fileName,"r",encoding="utf-8")
        data=f.readlines()
        f.close()
        times={}
        daytime=getTimeStr()
        ttTime=int(time.time())
        for line in data:
            line=line.strip()
            cr=line.split(",")
            tTime={}
            tTime["time"]=cr[1].strip()
            tTime["msg"]=cr[0].strip()
            tTime["ctime"]=getTimeStamp(daytime+" "+tTime["time"])
            if tTime["ctime"]<ttTime:
                tTime["ctime"]=tTime["ctime"]+dayTimeS
            
            times[tTime["time"]]=tTime
            print(tTime["ctime"])

        self.times=times

    def tick(self):
        global dayTimeS
        tTime=int(time.time())
        
        for timest in self.times:
            cTime=self.times[timest]
            if int(cTime["ctime"])<=tTime:
                cTime["ctime"]=int(cTime["ctime"])+dayTimeS
                print("next:"+str(cTime["ctime"]))
                notice(cTime["msg"])

      
def mainLoop():
    tT=TimeList()
    while(1):
        try:
            
            tT.tick()
            time.sleep(10)
        except Exception as e:
            print(e)
            time.sleep(5)


if __name__ == '__main__':
    mainLoop()
