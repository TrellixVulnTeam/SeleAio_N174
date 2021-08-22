# import threading
# import time
# import logging

# x = logging.basicConfig(level=logging.DEBUG)
# def foo():
   
#     logging.debug("starting %s",t.getName())
#     # time.sleep(5)
#     logging.debug("ending")

# if __name__ == "__main__":
#     t = threading.Thread(target=foo,name ="siyamak")
#     # t.setDaemon(True)
#     t.start()
#     main_thread = threading.current_thread()
#     for t in threading.enumerate():
#         if t is main_thread:
#             continue
#         logging.debug("threading true is %s", t.getName())
#         # t.join(2)


#     # x = threading.currentThread()
#     # print(x)
#     # t.setDaemon(True)

#     # t.join(2)
#     # print(t.is_alive())
#     # print(t.isDaemon())
#     # time.sleep(6)
#     # print(t.is_alive())
#     # print(t.isDaemon())

import threading
import queue
import time

# class N(threading.Thread):
#     def __init__(self, g):
#         threading.Thread.__init__(self)
#         self.g = g
#         self.ss = x
#     def run(self):
#         while True:
#             counter = self.g.get()
#             print("i recieved %s"%counter)
#             print("i recieved %s"%self.ss)
#             for i in range(counter):
#                 print("i am countin now: %s" %counter)
#             print(" im going to sleep for : %s" %counter)
#             time.sleep(counter)
#             print(" i slept for %s" %counter)
#             self.g.task_done()
# q = queue.Queue()

# for x in range(5):
#     print("create thread is %s" %x)
#     t = N(q)
#     # t.setDaemon(True)
#     t.start()
#     print("numeber of thread is %s" %x)

# for j in range(5):
#     q.put(j)
# # q.join()


