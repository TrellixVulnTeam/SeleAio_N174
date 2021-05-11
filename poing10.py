import asyncio
import aiohttp
import requests
import time
from extract_emails import ExtractEmails

# websites = """https://www.taekwondoforums.com/"""


with open('c.txt', 'r') as f:
    line = f.readlines()
    back_off = 60  # seconds to try again
    while True:
        for l in line:
            try:
                async def get(url):
                    try:
                        headers = {}
                        headers['Authorization'] = 'Basic xxxxxxx==='
                        headers['Content-Type'] = 'application/x-www-form-urlencoded'
                        headers['header1'] = 'somevalue'
                        async with aiohttp.ClientSession(raise_for_status=True, headers=headers) as session:
                            async with session.get(url=url) as response:
                                resp = await response.read()
                                print("Successfully got url {} with response of length {}.".format(
                                    url, len(resp)))
                                r = requests.get(l)
                                print(''.join(str(r)))
                                # await asyncio.sleep(back_off)
                                em = ExtractEmails(
                                    l, depth=None, print_log=False, ssl_verify=True, user_agent=None, request_delay=0.0)
                                print(em.emails)

                    except Exception as e:
                        print("Unable to get url {} due to {}.".format(
                            url, e.__class__))

                async def main(l):
                    ret = await asyncio.gather(*[get(l)])
                asyncio.run(main(l))
                # urls = websites.split("\n")
            except requests.exceptions.ReadTimeout:
                print("Too slow Mojo!")
