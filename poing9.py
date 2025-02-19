# # import asyncio

# # async def foo(number):
# #     print("start %d" % number)
# #     await asyncio.sleep(1)
# #     print("finished %d" % number)
# #     return str(number)


# import aiohttp
# import asyncio
# from extract_emails import ExtractEmails



# async def fetch(session, url):
#     async with session.get(url) as response:
#         em =ExtractEmails(url, depth = None, print_log=False, ssl_verify=True, user_agent=None, request_delay=0.0)
#         emails = em.emails
#         # if not emails:
#             # continue
#         # return await(emails)
#         return await response.email()

# async def main():
#     async with aiohttp.ClientSession() as session:
#         html = await fetch(session, 'http://python.org')
#         print(html)

# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())


import random
import asyncio
from aiohttp import ClientSession

async def fetch(url, session):
    async with session.get(url) as response:
        delay = response.headers.get("DELAY")
        date = response.headers.get("DATE")
        print("{}:{} with delay {}".format(date, response.url, delay))
        return await response.read()


async def bound_fetch(sem, url, session):
    # Getter function with semaphore.
    async with sem:
        await fetch(url, session)


async def run(r):
    url = "http://python.org"
    tasks = []
    # create instance of Semaphore
    sem = asyncio.Semaphore(1000)

    # Create client session that will ensure we dont open new connection
    # per each request.
    async with ClientSession() as session:
        for i in range(r):
            # pass Semaphore and session to every GET request
            task = asyncio.ensure_future(bound_fetch(sem, url.format(i), session))
            tasks.append(task)

        responses = asyncio.gather(*tasks)
        await responses

number = 10000
loop = asyncio.get_event_loop()

future = asyncio.ensure_future(run(number))
loop.run_until_complete(future)