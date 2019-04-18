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
from _thread import *
import _thread
import time
global b
b = (1,2)
def work_thread(a,x):

    cnt = 1
    global b
    b = (2,3)
    print ("Thread %d is runing..." )



print(type(b))
start_new_thread(work_thread,(1,2))

print ("Main thread doing an infinite wait loop...")

while True:
    print(b)

while True:
    pass