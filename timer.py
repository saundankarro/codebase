import time

timer = int(input("Enter a time in seconds: "))

def countdown(t):
    while t: 
        m, s = divmod(t,60)
        timer = f"{m:02d}:{s:02d}"
        print(timer, end = "\r")
        time.sleep(1)
        t  -= 1

    print(f"Fire in the hole")

countdown(timer)