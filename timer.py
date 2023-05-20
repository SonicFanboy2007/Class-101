import time
seconds = input("Enter the time in seconds")
2
def countdownTimer(seconds):
    while seconds > 0:
            m = int(seconds/60)
            s = int(seconds%60)
            timer = f'{m}:{s}'
            print (timer, end = '\r')
            time.sleep(1)
            seconds -= 1

  
    print("time up")

countdownTimer(int(seconds))