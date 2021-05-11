import requests
from extract_emails import ExtractEmails
import aiohttp
import asyncio
import eventlet
import contextlib
import time
import threading
# from requests_futures import sessions

# async def get(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             return await response.read()

def main():
    data = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3'}
    with open('c.txt', 'r') as f:
        line = f.readlines()
     
    for l in line:
        with eventlet.Timeout(2):
            try:
                r = requests.get(l,headers=data,timeout= 2) 
                if(r.status_code == 200):  
                    # print(r)
                    em =ExtractEmails(l, depth = None, print_log=False, ssl_verify=True, user_agent=None, request_delay=0.0)
                    emails = em.emails
                    print(emails)
            except:
                pass

if(__name__ == "__main__"):
    try:
        main()
        # t1 = threading.Thread(target=main()) 
        # t2 = threading.Thread(target=main) 
        # t1.start() 
    # starting thread 2 
        # t2.start() 
    except KeyboardInterrupt as e:
        print("Good Lock")
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.gather(*[get(l)]))
# این درسته
# https://eventlet.net/doc/examples.html#echo-server

# خروجی  خیلی ضعیف
