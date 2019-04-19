# from _thread import *
#
# def a(xx):
#     print("dsd")
#     global b
#     b = (2,3)
#
# b = (1,2)
#
# start_new_thread(a,(b))

#print(b)
from threading import Lock
from _thread import *
import _thread
import time
global b
b = (1,2)
mutex = Lock()
def work_thread(a,x,c):

    cnt = 1
    global b
    x= 1
    while True:
        b = (2,3)
    print ("Thread %d is runing..." )



print(type(b))
nums = (0,0,0)
start_new_thread(work_thread,nums)


print ("Main thread doing an infinite wait loop...")

time.sleep(3)
print(nums)
while b == (2,3):
    mutex.acquire()
    print(b)
    mutex.release()
while True:
    pass