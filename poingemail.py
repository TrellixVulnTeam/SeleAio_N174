import requests
from extract_emails import ExtractEmails
import time
import eventlet


def main():
    url_200 = []
    with open('c.txt', 'r', encoding='utf-8') as fp:
        data = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3'}
        line = fp.readlines()
    for i in line:
        l = i.split('\"')
        if len(l) > 1:
            # print("send requests : {}".format(i))
            with eventlet.Timeout(2):
                try:
                    r = requests.get(l[],headers=data,timeout= 2)
                    print(r.status_code)
                    
                
                except:
                    pass

if(__name__ == "__main__"):
    try:
        main()
    except KeyboardInterrupt as e:
        print("Good Lock")


            # # print(i)
            # time.sleep(5)
            # r = requests.get(i)
            # print(''.join(str(r)))
            # # print(i.status_code)
            # time.sleep(5)
            # em = ExtractEmails(i[:], depth=None, print_log=False,
            #                    ssl_verify=True, user_agent=None, request_delay=0.0)
            # emails = em.emails
            # print(emails)






# if line.__iter__('http'):
#     d = line
#     r = requests.get(d)
#     print(r.status_code)
# pass


# import os
# url = os.access("poing.txt", os.R_OK)
# files = {'file': open('poing.txt', 'r')}
# filename = 'poing.txt'
# f = open(filename, 'rU')
# from pathlib import PurePath

# Instantiate the PosixPath class
# f = PurePath('poing.txt')
# r = requests.get(f)
# print(r.status_code)
# import requests as req

# resp = req.request(method='GET', url=open('poing.txt', 'r'))
# print(resp.status_code)


# def url_response(url):
#     path, url = url
#     r = requests.get(url, stream = True)
#     with open(path, 'wb') as f:
#         for ch in r:
#             print(f.write(ch))

# pen(r'C:\Users\PC\Desktop\Beauti\poing.txt','r', encoding='cp1256') as fp:
#     line = fp.read().strip().split(",")
#     print(line)
#     r = requests.get(line)
#     print(r.status_code)
# for i in line:
#     print(i)
# cnt = 1
# while line:
# print("Line {}: {}".format(cnt, line.strip()))
# line = fp.readline()
#    cnt += 1
# import requests
# line = 'http://parsiankhazar.com'
# r = requests.get(line)
# print(r.status_code)
# for i in r:
#     em =ExtractEmails(i[:], depth=None, print_log=False, ssl_verify=True, user_agent=None, request_delay=0.0)
#     emails = em.emails
#     print(emails)

# import os
# if os.access("poing.txt", os.R_OK):
#     with open("poing.txt") as fp:
#         line=fp.read()
#         print(line)
# import requests

#     # with open('poing.txt','r', encoding='utf-8') as fp:
#     # line = fp.readline().strip().split("[,]")
# #     # print(line)
# r = requests.get(path="." + '/poing.txt')
# print(r.status_code)
