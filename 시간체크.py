## © 2021 RYU KANG <riukan121@google.com>, CC BY
import os

import time
from threading import Thread,Event
import pythoncom
import win32com.client
import json
import atexit
# 클래스로 정리해볼까
# 일과 보고 수정하는 기능도
# 로그 수동 수정도 가능하도록
# 10분 마다 로그 찍으면서 삑 하도록
# 실시간 시간흐름 표시는? (터미널 한줄 지우고, 다시 나오게 하고
# 로그 헤드만 계속 이어서 보여주고, 두가지 키 제공해서 빠져나가도록
# 매순간 로그 남겨서 가져오도록 하기 (에러시 이어서 시작할 수 있도록 로그 작성하고 꺼지도록)
# 날짜별로 기록 남겨서, 공부 기록 로그 남기기 (수정메뉴도)
# 카톡 챗봇으로 만들어볼까
# 파이썬으로 어플 못 만드나 아니면 어플처럼 파이썬 실행할 수 있게 하거나 카톡으로 파이썬 실행 결과 받는게 좋나
# sleep 버퍼 없애기
# 목표시간 설정 기능 (혹은 휴식 공부 시간설정 기능)(혹은 그때 그때 )
# 가끔 스레드가 자는 경우가 있네(콘솔 벗어나면 휴면 들어가나sleep상태에서 콘솔벗어나서?)
# 몇 분 휴식 및 공부했다고 띄우기
# 스페이스바는 인식하도록 만들기
# 터미널 보는 위치 (리스트 뽑았을 때 옮기는 것)
# 스레드로 잘못 입력하셨습니다 시간 지나면 사라지게 하기 + 종료중 ... 하나씩 나오게 하는 거
# help 만들기
# 임의 크기 조정하면 화면 크기 못 돌리는 것 방지(매 입력시 화면 크기 조정)
# 황금비율 적용
# 시간 재는거 윈도우에 서비스 등록으로?
# 해당 날짜 로그 검색
# 키설정도 하도록
# status 를 메인으로?
# 이름 입력할 수 있도록
# 알람 설정 기능 넣기
# 엔터로 바꿀까
# 휴식시간 공부시간 몇분 추가 기능
# 통계에서 시간을 계속 나타내기(~분째 공부중)
# 단축키 받기
# 그래프도 보여주도
# 입력을 바로 받는거 없나
# 한시간마다 일과체크 추가하는 것
# 백그라운드 재생과 단축키
# 경고창 모드
# 체크 놓치면 숫자 입력해서 빼는 시간 입력할 수 있도록
# 코딩 효율화 작업이 필요
# log에 flag를 두어서,한줄 추가 방식으로 하는게 나을까? 속도 비교
def vacant():
        pass
def savelog(w_s,w_all,r_s,r_all):
    
    with open("log.txt", "w") as f:
        
        
        if switch == True:
            ne = time.time() - w_s
        
            logs[today_date][0].append("\n\n%d시간 %d분째 공부 중"%(ne // 3600, (ne % 3600) // 60))
        
            logs[today_date][1] = [switch,w_s,w_all,r_s,r_all]
        
            
        else:
            re = time.time() - r_s
        
            logs[today_date][0].append("\n\n%d시간 %d분째 휴식 중"%(re // 3600, (re % 3600) // 60))
        
            logs[today_date][1] = [switch,w_s,w_all,r_s,r_all]
        
        
        
        json.dump(logs,f)
        
        
        
def tic(start,sch,schedule,fuc,tts):
    
    # 여기에 sleep 넣어서, 애초에 몇초간  들어가지 않게 하는 것도, 초기 딜레이 방지에 좋을 듯
    while not evt.isSet():
         
        lw = time.time()-start
        if  lw>3 and 0<=lw%1800 and lw%1800<3:
            
            print("\a", end="")

        a = fuc()    
        if sch != a:
            
            pythoncom.CoInitialize()                    
            tts.speak(f"{a} 할 시간 입니다.")
            pythoncom.CoUninitialize()
            
            sch = a
        
        
            
        time.sleep(2)
        
def toc(start,sch,schedule,fuc,tts):
    
    while not evt.isSet():
        lr = time.time()-start
        if lr>3 and 0<=lr%300 and lr%300<3:
            
            print("\a", end="")
        a = fuc()    
        if sch != a:
            
            pythoncom.CoInitialize()
            tts.speak(f"{a} 할 시간 입니다.")
            pythoncom.CoUninitialize()
            
            sch = a
            
        time.sleep(2)
        
def now_sch_f(t=1): # 스케줄에서 현재 시간에 해당하는 스케쥴 인덱스 return 
    global weekday
    a = schedule["시간"]
    ti = time.localtime()
    weekday_lst = ("월","화","수","목","금","토","일")
    weekday = weekday_lst[ti[6]]
    
    for i,x in enumerate(a):
                first = x.split(":")
                
                if int(first[0]) == ti[3] :
                    if int(first[1])>ti[4]:
                        if t == 2:
                                return schedule["시간"][i-1] if i-1 != -1 else "22:00"
                        else:
                                return schedule[weekday][i-1] if i-1 != -1 else "취침"
                        
                        
                elif int(first[0]) > ti[3]:
                        if t == 2:
                                return schedule["시간"][i-1] if i-1 != -1 else "22:00"
                        else:
                                return schedule[weekday][i-1] if i-1 != -1 else "취침"
    if t == 2:
            return "22:00"
    else:
            return "취침"
        
def show_schedule(s = "b"):
   
    len_sch_time = len(schedule["시간"])
    os.system(f"mode con cols=40 lines={49*(len_sch_time>19)+(len_sch_time<=19)*(len_sch_time*2+7)}")
    sch_str = "\n\n"
    temp_sch= now_sch_f(t=2)
    for i,x in zip(schedule["시간"],schedule[f"{weekday}"]):
        sch_str += f"{i} {x}\n\n" if temp_sch != i else f"==> {i} {x}\n\n"
    print(sch_str)
    input("\n돌아가려면 아무 키나 입력하십시오.")
    os.system("mode con cols=58 lines=10") if s != "a" else os.system("mode con cols=61 lines=13")
        
def start_screen(state,log,w_s,w_all,r_s,r_all,now_sch):
    global evt, th1, switch
    while True:

        a = input("="*60+"\n 공부 시간 체크 프로그램 V1.0.0 입니다. \n\n q = 공부 또는 휴식  w = 통계 e = 종료  L = 로그 s = 스케줄\n\n"+"="*60+"\n © 2021 RYU KANG <riukan121@google.com>, CC BY\n"+f"\n         '{now_sch}' 하는 시간 입니다.\n\n 공부를 시작하시겠습니까?  :  ")
        
        if a == "q":
            w_s = time.time()
            
                
            switch = True
            srt = time.strftime("%p %I:%M", time.localtime(w_s))
            evt = Event()
            
            th1 = Thread(target=tic,args=[w_s,now_sch,schedule,now_schf,tts])
            th1.daemon = True
            
            th1.start()
            
            
            log.append("#### "+srt+" 일과 시작")
            
                
            with open("log.txt", "w") as f:
                logs[today_date] = [log,[state,w_s,w_all,r_s,r_all]]
                json.dump(logs,f)

                
            os.system("mode con cols=58 lines=10")
            
            
            
            return state,log,w_s,w_all,r_s,r_all,now_sch

        elif a == "e":
            
                a = input("\n진짜로 끝내시겠습니까? y/n :  ")
                if a == "y":
                    state = False
                    return state,log,w_s,w_all,r_s,r_all,now_sch
                elif a == "n":
                    pass
        elif a == "L":
            print(" 아직 로그가 없습니다.")
        elif a == "w":
            print(" 아직 통계가 없습니다.")
        elif a == "s":
            show_schedule("a")
        else:
            print("\t            잘못 입력하셨습니다.")
            
def study_screen(state,log,w_s,w_all,r_s,r_all,now_sch):
        global th2,evt,switch
        
        while state:
            print("\n\n\n\n\n"+"-" * 19 + "%s 부터 공부중" % time.strftime("%p %I:%M", time.localtime(w_s)) + "-" * 19,end = "\n\n\n\n\n") 
            b = input("\t      휴식하려면 q를 입력하십시오 ")

            if b == "q":
                r_s = time.time()
                switch = False
                w_all += r_s - w_s
                print("\n\n\n\n\n\n\n\n\n시작 체크 완료, 이전 타이머 종료중..." ,end="\r")
                time.sleep(0.0001)
                evt.set()
                th1.join()
                evt = Event()
                th2 = Thread(target=toc,args=[r_s,now_sch,schedule,now_schf,tts])
                th2.daemon = True
                th2.start()
                
                
                
                
                
                
                

                log.append(" %d 시간 %d분 공부"%((r_s-w_s)//3600, ((r_s-w_s)%3600)//60))
                log.append("---- %s 휴식 시작"%(time.strftime("%p %I:%M", time.localtime(r_s))))
                
                with open("log.txt", "w") as f:
                    logs[today_date] = [log,[state,w_s,w_all,r_s,r_all]]
                    json.dump(logs,f)
                    
                now_sch = now_sch_f()
                
                return state,log,w_s,w_all,r_s,r_all,now_sch
            elif b == "w":  
                ne = time.time() - w_s
                nw = w_all + ne

                print("\n\t      현재 %d시간 %d분째 공부 중입니다. \n\n\n\t               일과 : %s \n\n\t           공부 누적 %d시간 %d분 \n\n\t           휴식 누적 %d시간 %d분 " % (ne // 3600, (ne % 3600) // 60, now_sch_f(), nw // 3600, (nw % 3600) // 60, r_all // 3600, (r_all % 3600) // 60))
                if nw // 3600 >= 8:
                    print("\n공부 시간 목표 달성")
                    if nw // 60 > 480:
                        print("공부 목표 시간 %d분 초과" % ((nw // 60) - 480))
                if r_all // 60 >= 100:
                    print("\n휴식시간 목표 달성")
                    if r_all // 60 > 100:
                        print("휴식 목표 시간 %d 초과" % ((r_all // 60) - 100))
                input("\n            돌아가려면 아무 키나 입력하십시오.")
        
                

            elif b == "e":  
                
                    a = input("\n진짜로 끝내시겠습니까? y/n :  ")
                    if a == "y":
                        nw = w_all + time.time() - w_s
                        print("\n\n\t            공부 누적 %d시간 %d분 \n\n\t            휴식 누적 %d시간 %d분" % (
                        nw // 3600, (nw % 3600) // 60, r_all // 3600, (r_all % 3600) // 60))
                        if nw // 3600 >= 8:
                            print("\n공부 시간 목표 달성")
                            if nw // 60 > 480:
                                print("공부 목표 시간 %d분 초과" % ((nw // 60) - 480))
                        if r_all // 60 >= 100:
                            print("\n휴식시간 목표 달성")
                            if r_all // 60 > 100:
                                print("휴식 목표 시간 %d 초과" % ((r_all // 60) - 100))
                        state = False
                        input("\n\n\n\n끝내려면 아무 거나 입력하시오.")
                        return state,log,w_s,w_all,r_s,r_all,now_sch
                    elif a == "n":
                        pass
            elif b == "L": 
                ne = time.time() - w_s
                os.system(f"mode con cols=40 lines={49*(len(log)>13)+(len(log)<=13)*(len(log)*2+10)}")
                print("\n"+"\n\n".join(log) + "\n\n\n%d시간 %d분째 공부 중"%(ne // 3600, (ne % 3600) // 60))
                input("\n\n\n돌아가려면 아무 키나 입력하십시오.")
                os.system("mode con cols=58 lines=10")
                
            elif b == "s":
                show_schedule()
                
            else:

                print("\t           잘못 입력하셨습니다.\n")
        return state,log,w_s,w_all,r_s,r_all,now_sch

def rest_screen(state,log,w_s,w_all,r_s,r_all,now_sch):
    
    global evt, th1,switch
    
    while state:
            print("\n\n\n\n\n\n"+"-" * 19 + "%s 부터 휴식중" % time.strftime("%p %I:%M", time.localtime(r_s)) + "-" * 19,end = "\n\n\n\n\n")
            c = input("\t      공부하려면 q를 입력하십시오 ")

            if c == "q":    
                w_s = time.time()
                switch = True
                r_all += w_s - r_s
                print("\n\n\n\n\n\n\n\n\n시작 체크 완료, 이전 타이머 종료중...",end="\r")
                time.sleep(0.0001)
                evt.set()
                th2.join()
                evt = Event()
                th1 = Thread(target=tic,args=[w_s,now_sch,schedule,now_schf,tts])
                th1.daemon = True
                th1.start()

                log.append("$$ %d 시간 %d분 휴식" % ((w_s - r_s) // 3600, ((w_s - r_s) % 3600) // 60))
                log.append("---- %s 공부 시작" % (time.strftime("%p %I:%M", time.localtime(w_s))))
                with open("log.txt", "w") as f:
                    
                    logs[today_date] = [log,[state,w_s,w_all,r_s,r_all]]
                    json.dump(logs,f)
                now_sch = now_sch_f()
                return state,log,w_s,w_all,r_s,r_all,now_sch
            elif c == "w":  ## 에스
                re = time.time() - r_s
                rw = r_all + re
                print("\n\t      현재 %d시간 %d분째 휴식 중입니다.\n\n\n\t                일과 : %s \n\n\t           공부 누적 %d시간 %d분 \n\n\t           휴식 누적 %d시간 %d분" % (re // 3600, (re % 3600) // 60, now_sch_f(), w_all // 3600, (w_all % 3600) // 60, rw // 3600, (rw % 3600) // 60))
                if w_all // 3600 >= 8:
                    print("\n공부 시간 목표 달성")
                    if w_all // 60 > 480:
                        print("공부 목표 시간 %d분 초과" % ((w_all // 60) - 480))
                if rw // 60 >= 100:
                    print("\n휴식시간 목표 달성")
                    if rw // 60 > 100:
                        print("휴식 목표 시간 %d분 초과" % ((rw // 60) - 100))
                input("\n            돌아가려면 아무 키나 입력하십시오.")

                

            elif c == "e":  
                
                    a = input("\n진짜로 끝내시겠습니까? y/n :  ")
                    if a == "y":
                        rw = r_all + time.time() - r_s
                        print("\n\n\t            공부 누적 %d시간 %d분 \n\n\t            휴식 누적 %d시간 %d분" % (
                            w_all // 3600, (w_all % 3600) // 60, rw // 3600,
                            (rw % 3600) // 60))
                        if w_all // 3600 >= 8:
                            print("\n공부 시간 목표 달성")
                            if w_all // 60 > 480:
                                print("공부 목표 시간 %d분 초과" % ((w_all // 60) - 480))
                        if r_all // 60 >= 100:
                            print("\n휴식시간 목표 달성")
                            if rw // 60 > 100:
                                print("휴식 목표 시간 %d분 초과" % ((rw // 60) - 100))
                        state = False
                        input("\n\n\n\n끝내려면 아무 거나 입력하시오.")
                        return state,log,w_s,w_all,r_s,r_all,now_sch
                    elif a == "n":
                        pass

            elif c == "L":  
                re = time.time() - r_s
                os.system(f"mode con cols=40 lines={49*(len(log)>13)+(len(log)<=13)*(len(log)*2+10)}")
                    
                print("\n"+"\n\n".join(log) + "\n\n\n%d시간 %d분째 휴식 중"%(re // 3600, (re % 3600) // 60))
                input("\n\n\n돌아가려면 아무 키나 입력하십시오.")
                os.system("mode con cols=58 lines=10")
                
            elif c == "s":
                show_schedule()
            else:
                
                print("\t           잘못 입력하셨습니다.\n")
    return state,log,w_s,w_all,r_s,r_all,now_sch
def new():
    global w_s,r_s
    
    state = True
    log = []
    srt = 0
    w_s = 0
    w_all = 0
    r_s = 0
    r_all = 0
    now_sch = now_sch_f()
    state,log,w_s,w_all,r_s,r_all,now_sch = start_screen(state,log,w_s,w_all,r_s,r_all,now_sch)
    while state:
   
        state,log,w_s,w_all,r_s,r_all,now_sch = study_screen(state,log,w_s,w_all,r_s,r_all,now_sch)
        state,log,w_s,w_all,r_s,r_all,now_sch = rest_screen(state,log,w_s,w_all,r_s,r_all,now_sch)
    atexit.register(savelog,w_s,w_all,r_s,r_all)
def cont():
    global evt, th1, th2
    
    log = logs[today_date][0]
    parms = logs[today_date][1]
    
    state = True
    w_s = parms[1]
    w_all = parms[2]
    r_s = parms[3]
    r_all = parms[4]
    now_sch = now_sch_f()
    st_or_rt = input("공부 시작  s, 휴식 시작  r ")
    while True:
        log.append("공백")
        if st_or_rt == "S" or st_or_rt == "s":
            
            
            w_s = time.time()
            log.append(f"이어서 {ti[3]}시 {ti[4]}분에 공부 시작")
            evt = Event()
            th1 = Thread(target=vacant())
            
            th1.start()
            os.system("mode con cols=58 lines=10")
            while state:
                
           
                state,log,w_s,w_all,r_s,r_all,now_sch = study_screen(state,log,w_s,w_all,r_s,r_all,now_sch)
                state,log,w_s,w_all,r_s,r_all,now_sch = rest_screen(state,log,w_s,w_all,r_s,r_all,now_sch)
            break
                
        elif st_or_rt == "R" or st_or_rt == "r":
            
            r_s = time.time()
            log.append(f"이어서 {ti[3]}시 {ti[4]}분에 휴식 시작")
            evt = Event()
            th2 = Thread(target=vacant())
            
            th2.start()
            os.system("mode con cols=58 lines=10")
            while state:
                
                state,log,w_s,w_all,r_s,r_all,now_sch = rest_screen(state,log,w_s,w_all,r_s,r_all,now_sch)   
                state,log,w_s,w_all,r_s,r_all,now_sch = study_screen(state,log,w_s,w_all,r_s,r_all,now_sch)
            break
    atexit.register(savelog,w_s,w_all,r_s,r_all)
if __name__ == '__main__':
    os.system("mode con cols=61 lines=12")
    ti = time.localtime()
    
    # 클릭 종료를 강제종료가 아니게 할 수 없나?
    with open("log.txt") as f:
        
        
        if not f.readline():
            
            logs = {}
        else :
            f.seek(0)
            logs = json.load(f)
        
        today_date = f"{ti[1]}{ti[2]}" # 0223
        
    
    tts = win32com.client.Dispatch("SAPI.SpVoice")
    now_schf = now_sch_f
    with open("schedule.txt","r", encoding='UTF-8') as js:
        schedule = json.load(js)
    
    
    
    
    
    
    
    if  today_date not in logs:
        
        new()
    else:
        while True:
            cont_bin= input(f"오늘 마지막 기록입니다. \n\n{logs[today_date][0][-1]}\n\n이어서 하시겠습니까? (Y/n) ")
            if (cont_bin == "Y" or cont_bin == "y") or cont_bin == "" :
                
                
                cont()
                break
                
            elif cont_bin == "n" or cont_bin == "N":
                new()
                break
            
        
    
    
    
    
                
    











