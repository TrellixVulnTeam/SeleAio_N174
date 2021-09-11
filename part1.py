import requests
import json
from bs4 import BeautifulSoup
from extract_emails import EmailExtractor
from extract_emails.browsers import RequestsBrowser
import smtplib, ssl
import re
from concurrent.futures import ThreadPoolExecutor

ltags=[]
def extractatag(url):
    ### extract 'atags' from each url and add them to 'ltags' list###
    try:
        simpurl = url.strip()
        x = requests.get(simpurl, timeout=200)
        soup = BeautifulSoup(x.content, "html.parser")
        ltag = soup.find_all("a")
        for i in ltag:
            ltags.append(i)
            print(i)
    except Exception as err:
        print(err)

exmaili = []
def extractemail(atag):
    ###extract emails from each links in each url###
    lhref=atag.get("href")
    with RequestsBrowser() as browser:
        email_extractor = EmailExtractor(lhref, browser, depth=2)
        emails = email_extractor.get_emails()
    for email in emails:
        exmai = email.as_dict()["email"]
        if not exmai in exmaili:
            exmaili.append(exmai)
        print(exmai)

# این اکی نیست
