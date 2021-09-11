import threading
import requests
from datetime import datetime
import eventlet
from bs4 import BeautifulSoup
from extract_emails import EmailExtractor
from extract_emails.browsers import RequestsBrowser

  
def foo():
    data = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3'}
    with open('c.txt', 'r') as f:
        line = f.readlines()
    start = datetime.now()
    for l in line[0:50]:
        
          
                r = requests.get(l.strip(),headers=data,timeout= 2)
            
          
                soup = BeautifulSoup(r.content, "html.parser")
                ltags = soup.find_all("a")
                try:
                    for tag in ltags:
                        lhref = tag.get("href")
                        with RequestsBrowser() as browser:
                            email_extractor = EmailExtractor(lhref, browser, depth=2)
                            emails = email_extractor.get_emails()
                        for email in emails:
                            print(email)
                        
                except Exception as err:
                    print(err)

           
                
       
  
    end =  datetime.now()
    print("result of time is:", end-start)

if __name__ == "__main__":
    # t = threading.Thread(target = foo, name="Siyamak" )
    foo()
    # این تست است