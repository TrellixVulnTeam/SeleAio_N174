# import requests
# import time

# def download_site(url, session):
#             with session.get(url) as response:
#                         print(f"Read {len(response.content)} from {url}")

# def download_all_sites(sites):
#             with requests.Session() as session:
#                         for url in sites:
#                                     download_site(url, session)

# if __name__ == "__main__":
#             sites = [
#                         "http://www.jython.org",
#                         "http://olympus.realpython.org/dice",
#             ] 
#             start_time = time.time()
#             download_all_sites(sites)
#             duration = time.time() - start_time
#             print(f"Downloaded {len(sites)} in {duration} seconds")

# # more speed


# import concurrent.futures
# import requests
# import threading
# import time

# thread_local = threading.local()

# def get_session():
#             if not getattr(thread_local, "session", None):
#                         thread_local.session = requests.Session()
#             return thread_local.session

# def download_site(url):
#             session = get_session()
#             with session.get(url) as response:
#                         print(f"Read {len(response.content)} from {url}")

# def download_all_sites(sites):
#             with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
#                         executor.map(download_site, sites)

# if __name__ == "__main__":
#             sites = [
#                         "http://www.jython.org",
#                         "http://olympus.realpython.org/dice",
#             ] 
#             start_time = time.time()
#             download_all_sites(sites)
#             duration = time.time() - start_time
#             print(f"Downloaded {len(sites)} in {duration} seconds")







# import asyncio
# import time
# import aiohttp

# async def download_site(session, url):
#             async with session.get(url) as response:
#                         print("Read {0} from {1}".format(response.content_length, url))

# async def download_all_sites(sites):
#             async with aiohttp.ClientSession() as session:
#                         tasks = []
#                         for url in sites:
#                                     task = asyncio.ensure_future(download_site(session, url))
#                                     tasks.append(task)
#                         await asyncio.gather(*tasks, return_exceptions=True)

# if __name__ == "__main__":
#             sites = [
#                         "http://www.jython.org",
#                         "http://olympus.realpython.org/dice",
#             ] 
#             start_time = time.time()
#             asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
#             duration = time.time() - start_time
#             print(f"Downloaded {len(sites)} sites in {duration} seconds")




# client
# import aiohttp
# import asyncio

# async def fetch(session, url):
#     async with session.get(url) as response:
#         return await response.text()

# async def main():
#     async with aiohttp.ClientSession() as session:
#         html = await fetch(session, 'http://python.org')
#         print(html)

# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())


# server
# from aiohttp import web

# async def handle(request):
#     name = request.match_info.get('name', "Anonymous")
#     text = "Hello, " + name
#     return web.Response(text=text)

# app = web.Application()
# app.add_routes([web.get('/', handle),
#                 web.get('/{name}', handle)])

# if __name__ == '__main__':
#     web.run_app(app)





import aiohttp
import asyncio
from extract_emails import ExtractEmails

async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response.read()
            em =ExtractEmails(url, depth = None, print_log=False, ssl_verify=True, user_agent=None, request_delay=0.0)
            emails = em.emails
            # if not emails:
                # continue
            # print(emails)
            return await email


loop = asyncio.get_event_loop()

coroutines = [get("https://www.taekwondoforums.com/")]

results = loop.run_until_complete(asyncio.gather(*coroutines))
asyncio.run(get(l))
print("Results: %s" % results)







