# import re
# x = ['+5556', '-1539', '-99','+1500', '45+34-12+']
# x = [re.sub('[+-]', '', item) for item in x]
# print(x)






# lst = [("aaaa8"),("bb8"),("ccc8"),("dddddd8")]
# print([s.strip('8') for s in lst]) # remove the 8 from the string borders
# print([s.replace('8', '') for s in lst]) # remove all the 8s
# lst = [("aaaa8"),("bb8"),("ccc8"),("dddddd8")]
# mylst = set(map(lambda each:each.strip("8"), lst))
# print (mylst)









# import pytest
# mylist = [("ccc8"),("aaaa8"),("bb8"),("ccc8"),("dddddd8")]
# mylist = '\n'.join(set(mylist))
# print (mylist)
# @pytest.mark.timeout(300)
# def test_foo():
#     pass



import requests
import time

# start = time.time()
# session = requests.Session()
# p = session.get("http://httpbin.org/get")
# end = time.time()
# print(end - start)
# print(p)


# start = time.time()
# o = requests.get("http://httpbin.org/get")  
# end = time.time()
# print(end - start)
# print(o)


# start = time.time()
# session = requests.Session()
# adapter = requests.adapters.HTTPAdapter(
#     pool_connections=100,
#     pool_maxsize=100)
# session.mount('http://', adapter)
# k = session.get('http://httpbin.org/get', timeout=5)
# end = time.time()
# print(end - start)
# print(k)


from extract_emails import EmailExtractor
from extract_emails.browsers import RequestsBrowser


with RequestsBrowser() as browser:
    email_extractor = EmailExtractor("http://www.tomatinos.com/", browser, depth=2)
    emails = email_extractor.get_emails()


for email in emails:
    print(email)
    print(email.as_dict())