import threading
import requests
from datetime import datetime
from extract_emails import ExtractEmails
import eventlet
import logging
#Create and configure logger
# logging.basicConfig(level=logging.DEBUG)
  
# #Creating an object
# logger=logging.getLogger()
  
# #Setting the threshold of logger to DEBUG
# logger.setLevel(logging.DEBUG)
  
def foo():
    data = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3'}
    with open('c.txt', 'r') as f:
        line = f.readlines()
    start = datetime.now()
    for l in line[0:70]:
        with eventlet.Timeout(2):
            try:
                r = requests.get(l,headers=data,timeout= 2)
                print(r,t.getName())
                # if(r.status_code == 200):  
                    # print(r,t.getName())
                    # logger.info("Just an information  : %s", t.getName())
                    # em =ExtractEmails(l, depth = None, print_log=False, ssl_verify=True, user_agent=None, request_delay=0.0)
                    # emails = em.emails
                    # print(emails)
            
                # else:
                    # pass
                    # logger.warning("Its a Warning is %s", t.getName())
            except:
                pass
                # logger.debug("Harmless debug Message is %s", t.getName())
    # 
        pass
  
    end =  datetime.now()
    print("result of time is:", end-start, t.getName())

if __name__ == "__main__":
    t = threading.Thread(target = foo, name="Siyamak" )
    t.start()
def bar():
    data = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3'}
    with open('c.txt', 'r') as f:
        line = f.readlines()
    start = datetime.now()

    for l in line[70:140]:
        with eventlet.Timeout(2):
            try:
                r = requests.get(l,headers=data,timeout= 2)
                print(r,t2.getName())
                # if(r.status_code == 200):  
                #     print(r,t2.getName())
                    # logger.info("Just an information  : %s", t.getName())
                    # em =ExtractEmails(l, depth = None, print_log=False, ssl_verify=True, user_agent=None, request_delay=0.0)
                    # emails = em.emails
                    # print(emails)
            
                # else:
                    # pass
                    # logger.warning("Its a Warning is %s", t.getName())
            except:
                pass
                # logger.debug("Harmless debug Message is %s", t.getName())
    # 
        pass
  
    end =  datetime.now()
    print("result of time is:", end-start,t2.getName())

if __name__ == "__main__":
    # t = threading.Thread(target = foo, name="Siyamak" )
    t2 = threading.Thread(target = bar,name="diyana")
    t2.start()

    
def mar():
    data = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3'}
    with open('c.txt', 'r') as f:
        line = f.readlines()
    start = datetime.now()

    for l in line[140::]:
        with eventlet.Timeout(2):
            try:
                r = requests.get(l,headers=data,timeout= 2)
                print(r,t3.getName())
                # if(r.status_code == 200):  
                #     print(r,t2.getName())
                    # logger.info("Just an information  : %s", t.getName())
                    # em =ExtractEmails(l, depth = None, print_log=False, ssl_verify=True, user_agent=None, request_delay=0.0)
                    # emails = em.emails
                    # print(emails)
            
                # else:
                    # pass
                    # logger.warning("Its a Warning is %s", t.getName())
            except:
                pass
                # logger.debug("Harmless debug Message is %s", t.getName())
    # 
        pass
  
    end =  datetime.now()
    print("result of time is:", end-start,t2.getName())

if __name__ == "__main__":
    # t = threading.Thread(target = foo, name="Siyamak" )
    t3 = threading.Thread(target = mar,name="sami") 
    t3.start()
   


