import requests
from extract_emails import ExtractEmails
import aiohttp
import asyncio


with open('c.txt', 'r') as f:
    line = f.readlines()
    while True:
        for l in line:
                try:
                    async def get(url):
                        async with aiohttp.ClientSession() as session:
                            async with session.get(url) as response:
                                return await response.read()

                    loop = asyncio.get_event_loop()
                    coroutines = [get(l)]
                    results = loop.run_until_complete(asyncio.gather(*coroutines))
                    em =ExtractEmails(l, depth = None, print_log=False, ssl_verify=True, user_agent=None, request_delay=0.0)
                    emails = em.emails
                    print(emails)
                    print("Results: %s" % results)

                except requests.exceptions.ReadTimeout :
                    print ("Too slow Mojo!")
# تست است