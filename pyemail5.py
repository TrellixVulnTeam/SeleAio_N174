import requests
from extract_emails import ExtractEmails
import aiohttp
import asyncio
import ssl
import certifi
import time

# ssl_context = ssl.create_default_context(cafile=certifi.where())
bad_fp = b'0'
exc = None


async def main():
    with open('c.txt', 'r') as f:
        line = f.readlines()
        while True:
            for l in line:

                ssl_context = ssl.create_default_context(
                    cafile=certifi.where())
                async with aiohttp.ClientSession() as session:
                    async with session.get(l) as resp:
                        if(resp.status == 200):

                            em = ExtractEmails(
                                l, depth=None, print_log=False, ssl_verify=True, user_agent=None, request_delay=0.0)
                            emails = em.emails
                            print(emails)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
if __name__ == "__main__":
    t1 = threading.Thread(target = main)
    t2 = threading.Thread(target = main)
    t3 = threading.Thread(target = main)
    t4 = threading.Thread(target = main)
    t1.start()
    t2.start()
    t3.start()
    t4.start()