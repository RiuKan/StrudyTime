import atexit

def he():
    
    a = 2
    
    a = change(a)
    atexit.register(hey,a)
    print("done")

def hey(a):
    input(a)
def change(a):
    a = 3
    return a
he()
