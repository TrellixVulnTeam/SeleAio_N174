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

def foo():
    for i in range(20):
        print(i, t.getName())
    
    for j in range(20,50):
        print(j, t1.getName())

if __name__ =="__main__":
    t = threading.Thread(target = foo, name="siyamak")
    t1 = threading.Thread(target = foo, name="diyana")
    t.start()
    t1.start()