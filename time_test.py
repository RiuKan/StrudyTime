import time
import timeit
a = {}
b = []
for i in range(10000):
    a[i] = []
    b.append(f"{i}")


def t1():
    "1999" in a
    
    
def t2():
    "1999" in b

    
print(timeit.timeit('t1()',number=1,globals=globals()))
print(timeit.timeit('t2()',number=1,globals=globals()))

# 리스트 와 딕셔너리에서 in 으로 찾는건, 길이에 상관없는 딕셔너리(랜덤 시간)가 유리하다. 


        
        
