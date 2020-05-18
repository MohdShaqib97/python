from threading import *

########## creating thread without using thread class ###########
def display():
    for i in range(10):
        print("child thread")

t = Thread(target = display)
t.start()
for i in range(10):
    print("Main thread")

########## creating thread using thread class ###########
class myThread(Thread):
    def run(self):
        for i in range(10):
            print("Child Thread")
t = myThread()
t.start()
for i in range(10):
    print("Main Thread")

########## creating thread without extending thread class ###########
class test:
    def display(self):
        for i in range(10):
            print("Child Thread")

obj = test()
t = Thread(target = obj.display)
t.start()
for i in range(10):
    print("Main Thread")