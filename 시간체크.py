## © 2021 RYU KANG <riukan121@google.com>, CC BY
import os
import time
from threading import Thread,Event

def tic(start):
   
    # 여기에 sleep 넣어서, 애초에 몇초간  들어가지 않게 하는 것도, 초기 딜레이 방지에 좋을 듯
    while not evt.isSet():
         
        lw = time.time()-start
        if lw>3 and 0<=lw%1800 and lw%1800<3:
            
            print("\r\t      공부한지 %d 분이 지났습니다. : \a" %(lw//60), end="")
    # 중간에 로그나 통계 볼 때 태그 조정해서 끄던지, 소리만 나게 하던지 하기 
        time.sleep(3)
        
def toc(start):

    while not evt.isSet():
        lr = time.time()-start
        if lr>3 and 0<=lr%300 and lr%300<3:
            
            print("\r\t       휴식한지 %d 분이 지났습니다 : \a"%(lr//60), end="")
        time.sleep(3)
    
if __name__ == '__main__':
    os.system("mode con cols=61 lines=13")
    state = True

    log = []
    srt = 0
    w_s = 0
    w_all = 0
    r_s = 0
    r_all = 0
    while state:

        a = input("="*60+"\n 공부 시간 체크 프로그램 V1.0.0 입니다. \n\n q = 공부 또는 휴식  s = 통계 e = 종료  L = 로그\n\n"+"="*60+"\n © 2021 RYU KANG <riukan121@google.com>, CC BY\n"+"\n\n\n\n 공부를 시작하시겠습니까?  :  ")
        
        if a == "q":
            w_s = time.time()
            srt = time.strftime("%p %I:%M", time.localtime(w_s))
            evt = Event()
            
            th1 = Thread(target=tic,args=[w_s])
            th1.daemon = True
            
            th1.start()
            
            
            log.append("#### "+srt+" 일과 시작")
            os.system("mode con cols=58 lines=10")
            
            print("\n\n\n\n\n"+"-" * 19 + "%s 부터 공부중" % srt + "-" * 19,end = "\n\n\n\n\n")
            
            break

        elif a == "e":
            while True:
                a = input("\n진짜로 끝내시겠습니까? y/n :  ")
                if a == "y":
                    state = False
                    break
                elif a == "n":
                    break
        elif a == "L":
            print(" 아직 로그가 없습니다.")
        elif a == "s":
            print(" 아직 통계가 없습니다.")
        else:
            print("잘못 입력하셨습니다.")
######## 휴식
    while state:

        while state:
            b = input("\t      휴식하려면 q를 입력하십시오 ")

            if b == "q":  ## 큐
                r_s = time.time()
                w_all += r_s - w_s
                print("\n\n\n\n\n\n\n\n\n시작 체크 완료, 이전 타이머 종료중..." ,end="\r")
                time.sleep(0.0001)
                evt.set()
                th1.join()
                evt = Event()
                th2 = Thread(target=toc,args=[r_s])
                th2.daemon = True
                th2.start()
                
                
                
                
                
                
                

                log.append(" %d 시간 %d분 공부"%((r_s-w_s)//3600, ((r_s-w_s)%3600)//60))
                log.append("---- %s 휴식 시작"%(time.strftime("%p %I:%M", time.localtime(r_s))))
        ## 1
                print("\n\n\n\n\n\n"+"-" * 19 + "%s 부터 휴식중" % time.strftime("%p %I:%M", time.localtime(r_s)) + "-" * 19,end = "\n\n\n\n\n")
                break
            elif b == "s":  ## 에스
                ne = time.time() - w_s
                nw = w_all + ne

                print("\n\t      현재 %d시간 %d분째 공부 중입니다. \n\n\n\t           일과 시작: %s \n\n\t           공부 누적 %d시간 %d분 \n\n\t           휴식 누적 %d시간 %d분 " % (ne // 3600, (ne % 3600) // 60, srt, nw // 3600, (nw % 3600) // 60, r_all // 3600, (r_all % 3600) // 60))
                if nw // 3600 >= 8:
                    print("\n공부 시간 목표 달성")
                    if nw // 60 > 480:
                        print("공부 목표 시간 %d분 초과" % ((nw // 60) - 480))
                if r_all // 60 >= 100:
                    print("\n휴식시간 목표 달성")
                    if r_all // 60 > 100:
                        print("휴식 목표 시간 %d 초과" % ((r_all // 60) - 100))
                input("\n            돌아가려면 아무 키나 입력하십시오.")
        ## 2
                print("\n\n\n\n\n\n" + "-" * 19 + "%s 부터 공부중" % time.strftime("%p %I:%M", time.localtime(w_s)) + "-" * 19,end = "\n\n\n\n\n")

            elif b == "e":  ## 이
                while True:
                    a = input("\n진짜로 끝내시겠습니까? y/n :  ")
                    if a == "y":
                        nw = w_all + time.time() - w_s
                        print("\n공부 누적 %d시간 %d분 \n\n휴식 누적 %d시간 %d분" % (
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
                        input("끝내려면 아무 거나 입력하시오.")
                        break
                    elif a == "n":

        ## 3
                        print("\n\n\n\n\n\n" + "-" * 19 + "%s 부터 공부중" % time.strftime("%p %I:%M", time.localtime(w_s)) + "-" * 19,end = "\n\n\n\n\n")
                        break
            elif b == "L": ## 엘
                ne = time.time() - w_s
                os.system(f"mode con cols=40 lines={49*(len(log)>13)+(len(log)<=13)*(len(log)*2+10)}")
                print("\n"+"\n\n".join(log) + "\n\n\n%d시간 %d분째 공부 중"%(ne // 3600, (ne % 3600) // 60))
                input("\n\n\n돌아가려면 아무 키나 입력하십시오.")
                os.system("mode con cols=58 lines=10")

        ## 4
                print("\n\n\n\n\n\n" + "-" * 19 + "%s 부터 공부중" % time.strftime("%p %I:%M", time.localtime(w_s)) + "-" * 19,end = "\n\n\n\n\n")
            else:

        ## 5
                
                print("\n\n\n\n" + "-" * 19 + "%s 부터 공부중" % time.strftime("%p %I:%M", time.localtime(w_s)) + "-" * 19,end = "\n\n\n")
                print("\t           잘못 입력하셨습니다.\n")
######## 공부
        while state:
            c = input("\t      공부하려면 q를 입력하십시오 ")

            if c == "q":    ## 큐
                w_s = time.time()
                r_all += w_s - r_s
                print("\n\n\n\n\n\n\n\n\n시작 체크 완료, 이전 타이머 종료중...",end="\r")
                time.sleep(0.0001)
                evt.set()
                th2.join()
                evt = Event()
                th1 = Thread(target=tic,args=[w_s])
                th1.daemon = True
                th1.start()

                log.append("$$ %d 시간 %d분 휴식" % ((w_s - r_s) // 3600, ((w_s - r_s) % 3600) // 60))
                log.append("---- %s 공부 시작" % (time.strftime("%p %I:%M", time.localtime(w_s))))
        ## 6
                print("\n\n\n\n\n\n"+"-" * 19 + "%s 부터 공부중" % time.strftime("%p %I:%M", time.localtime(w_s)) + "-" * 19,end = "\n\n\n\n\n")
                break
            elif c == "s":  ## 에스
                re = time.time() - r_s
                rw = r_all + re
                print("\n\t      현재 %d시간 %d분째 휴식 중입니다.\n\n\n\t           일과 시작: %s \n\n\t           공부 누적 %d시간 %d분 \n\n\t           휴식 누적 %d시간 %d분" % (re // 3600, (re % 3600) // 60, srt, w_all // 3600, (w_all % 3600) // 60, rw // 3600, (rw % 3600) // 60))
                if w_all // 3600 >= 8:
                    print("\n공부 시간 목표 달성")
                    if w_all // 60 > 480:
                        print("공부 목표 시간 %d분 초과" % ((w_all // 60) - 480))
                if rw // 60 >= 100:
                    print("\n휴식시간 목표 달성")
                    if rw // 60 > 100:
                        print("휴식 목표 시간 %d분 초과" % ((rw // 60) - 100))
                input("\n            돌아가려면 아무 키나 입력하십시오.")
        ## 7
                print("\n\n\n\n\n\n" + "-" * 19 + "%s 부터 휴식중" % time.strftime("%p %I:%M", time.localtime(r_s)) + "-" * 19,end = "\n\n\n\n\n")

                

            elif c == "e":  ## 이
                while state:
                    a = input("\n진짜로 끝내시겠습니까? y/n :  ")
                    if a == "y":
                        rw = r_all + time.time() - r_s
                        print("\n공부 누적 %d시간 %d분 \n\n휴식 누적 %d시간 %d분" % (
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
                        input("끝내려면 아무 거나 입력하시오.")
                        break
                    elif a == "n":

        ## 8
                        print("\n\n\n\n\n\n" + "-" * 19 + "%s 부터 휴식중" % time.strftime("%p %I:%M", time.localtime(r_s)) + "-" * 19,end = "\n\n\n\n\n")

                        break

            elif c == "L":  ## 엘
                re = time.time() - r_s
                os.system(f"mode con cols=40 lines={49*(len(log)>13)+(len(log)<=13)*(len(log)*2+10)}")
                    
                print("\n"+"\n\n".join(log) + "\n\n\n%d시간 %d분째 휴식 중"%(re // 3600, (re % 3600) // 60))
                input("\n\n\n돌아가려면 아무 키나 입력하십시오.")
                os.system("mode con cols=58 lines=10")

        ## 9
                print("\n\n\n\n\n\n" + "-" * 19 + "%s 부터 휴식중" % time.strftime("%p %I:%M", time.localtime(r_s)) + "-" * 19,end = "\n\n\n\n\n")
            else:

        ## 10
                print("\n\n\n\n" + "-" * 19 + "%s 부터 휴식중" % time.strftime("%p %I:%M", time.localtime(r_s)) + "-" * 19,end = "\n\n\n")
                print("\t           잘못 입력하셨습니다.\n")
                
    











