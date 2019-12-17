import asyncio
import aiohttp
import requests
import time
from extract_emails import ExtractEmails

# websites = """https://www.taekwondoforums.com/"""


with open('c.txt', 'r') as f:
    line = f.readlines()
    while True:
        for l in line:
                try:
                    async def get(url):
                        try:
                            async with aiohttp.ClientSession() as session:
                                async with session.get(url=url) as response:
                                    resp = await response.read()
                                    print("Successfully got url {} with response of length {}.".format(url, len(resp)))
                                                        # print("Finalized all. ret is a list of len {} outputs.".format(len(ret)))
                                    em =ExtractEmails(l, depth = None, print_log=False, ssl_verify=True, user_agent=None, request_delay=0.0)
                                    emails = em.emails
                                    print(emails)
                        except Exception as e:
                            print("Unable to get url {} due to {}.".format(url, e.__class__))


                            asyncio.run(get(l))
                except requests.exceptions.ReadTimeout :
                        print ("Too slow Mojo!")
# async def main(l):
#     ret = await asyncio.gather(*[get(l)])
                    # urls = websites.split("\n")