import urllib
from bs4 import BeautifulSoup


# url ="https://shalishomal.ir"
# x = urllib.request.urlopen(url)
# print(x.status)
# print(x.info())



# soup = BeautifulSoup(x, "html.parser")
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.link['href'])
# print(soup.img['src'])




# پارسه در پایتون
# from urllib.parse import urlparse


# url = "https://python.org"
# x = urlparse(url)
# print(x.scheme)
# print(x.netloc)
# print(x.path)
# x._replace(scheme='http')
# print(x)



# from urllib.parse import urlsplit

# url = "http://python.org"
# x = urlsplit(url)
# print(x)
# print(x.geturl())



# from urllib.parse import urljoin

# url = "https://python.org"
# x = urljoin(url,"siyamak.html")
# print(x)


# import urllib
# from urllib.request import urlopen
# import urllib.request, urllib.parse, urllib.error 
# from bs4 import BeautifulSoup

# x =urlopen("https://www.ngkntk.co.jp").read()
# y = BeautifulSoup(x , "html.parser")


# for link in y.find_all("a"):
#     z = link.get("href")
#     print(z)
#     print("================================================")

# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# url = 'https://shalishomal.ir'
# x = urlopen(url)
# soup = BeautifulSoup(x,'html.parser')
# # print(soup.link)
# # print(soup.prettify())
# # print(soup.title)
# # print=(soup.link['href'])
# print(soup.html.body.div.div)



# import mechanize

# brow = mechanize.Browser()
# brow.open("https://python.org")
# # for form in brow.forms():
# #     print(form)
# # print(dir(brow))
# brow.select_form(nr= 0)
# # brow.form['s'] ="python"
# brow.submit()
# # for link in brow.links():
# #     print(link.url)

# for link in brow.links():
#     if "python" in link.url:
#         print(link.url)