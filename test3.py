import atexit
import os
def at_exit_func():
    print ("exited.")
    os.system("Pause")

def main():
    print("End")


if __name__ == '__main__':
    atexit.register(at_exit_func)
    main()


