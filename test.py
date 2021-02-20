import json
import time
import timeit
import os
import win32com.client

from playsound import playsound
with open("schedule.txt","r", encoding='UTF-8') as js:
        schedule = json.load(js)
schedule["시간"]

def t1():
    # time.strptime(schedule["시간"][0],"%H:%M")
    #b = str(time.localtime()[3])+":"+str(time.localtime()[4])
    schedule["시간"][3]
    schedule["시간"][4]
    
    
def t2():
    #a = time.strftime("%H:%M",time.localtime())
    a = schedule["시간"]
    a[3]
    a[4]
def time_index():
    global schedule
    a = schedule["시간"]
    ti = time.localtime()
    for i,x in enumerate(a):
        first = x.split(":")
        
        if int(first[0]) == ti[3] :
            if int(first[1])>ti[4]:
                return i-1
                break
            else:
                return i
                break
                
        elif int(first[0]) > ti[3]:
            return i-1
            break     
    
print(timeit.timeit('time_index()',number=1,globals=globals()))
print(timeit.timeit('t2()',number=1,globals=globals()))


playsound("./취침.mp3")




playsound("./취침.mp3")

        
        
