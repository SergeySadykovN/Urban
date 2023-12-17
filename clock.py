import time


# while True:
#     now = time.localtime()
#     print('Current time:', time.strftime("%H:%M:%S", now))
#     time.sleep(1)

def time_display():
    now = time.localtime()
    print('Current time:', time.strftime("%H:%M:%S", now))
    time.sleep(1)
    # print(time.strptime('Time is', '%d:%m:%Y:%H:%M:%S'),now)

while True:
    time_display()
