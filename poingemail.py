import requests
from extract_emails import ExtractEmails

with open('vyt.txt','r', encoding='utf-8') as fp:
    line = fp.readline().strip().split("],[")
    for i in line:
        print(i)
    r= requests.get(line)
    print(r.status_code)
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
