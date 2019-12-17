import requests
from extract_emails import ExtractEmails


with open('shango.txt', 'r') as f:
    line = f.readline()
    # for u in line:
    #     r= requests.get(u)
    #     print(r.status_code)

    


    for l in line:
        # print(l)
        em =ExtractEmails(l[:], depth = None, print_log=False, ssl_verify=True, user_agent=None, request_delay=0.0)
        emails = em.emails
        print(emails)


        # جواب نمی ده مادامی ما ریدلاین گداشتیم .و از حلقه فور استفاده کردیم باید رید لاینز کنیم و همینطوز در صفحه تکس نباید ویرگول بزاریم