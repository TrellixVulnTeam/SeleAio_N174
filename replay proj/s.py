# my script :)

import requests
from datetime import datetime
from time import sleep
import requests 
from requests.adapters import TimeoutSauce
import eventlet
from extract_emails import ExtractEmails



def main():
    url_200 = []
    data = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3'}
    with open('status.rtf') as f:
        lists = f.readlines()
    start = datetime.now()
    print("start of time:",start)
    for i in lists:
        l = i.split('\"')
        if len(l) > 1:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            # print("send requests : {}".format(l[1]))
            
            with eventlet.Timeout(2):
                try:
                    r = requests.get(l[1],headers=data,timeout= 2)
                    
                    if(r.status_code == 200):
                        url_200.append(l[1])
                    
                        print("[T]: {} |> site : {} >> response : {}".format(current_time,l[1],r.status_code))
                        # em = ExtractEmails(l, depth=None, print_log=False, ssl_verify=True, user_agent=None, request_delay=0.0)
                        # emails = em.emails
                        # print("[T]: {} |> site : {} >> response : {}".format(current_time,l[1],r.emails))
                        # print(emails)
                    
                except:
                    pass
            
            print("find 200 response : {}".format(len(url_200)))
            end =  datetime.now()
            print("end of time:",end)
            print("result of time is:", end-start)

         
           

if(__name__ == "__main__"):
    try:
        main()
    except KeyboardInterrupt as e:
        print("Good Lock")


    # خروجی اصلا خوب نیست