import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    
    print ("Timer completed!")

user_input = input("Enter the time in seconds: ")

if user_input.isdigit():
    t = int(user_input)
    countdown(t)
else:
    print("Invalid input! Please enter numbers only.")