
# # async def mycro(number):
# #     print("start %d" % number)
# #     await asyncio.sleep(1)
# #     print("finished %d" % number)
# #     return str(number)

# # task = asyncio.ensure_future(mycro(2))
# # loop = asyncio.get_event_loop()
# # loop.run_until_complete(task)
# # loop.close()
# # asyncio.run(mycro(3))
# # asyncio.run(mycro(4))


# # async def bar():
# #     print("start bar")
# #     await asyncio.sleep(1)
# #     print("stop bar")
# # async def mod():
# #     print("start mod")
# #     await bar()
# #     print("stop mod")
# # asyncio.run(mod())


# from aiohttp import ClientSession
# import asyncio

# async def fetch(url):
#     async with ClientSession() as s, s.get(url) as res:
#         ret = await res.read()
#         # print(ret)
#         return ret
# # asyncio.run(fetch("http://python.org"))

# async def print_when_done(tasks):
#     for res in limited.as_completed(tasks,10):
#         print(await res)

# coros = [
#     fetch("http://python.org")
#     for i in range(10)
# ]


# def limited_as_completed(coros, limit):
#     futures = [
#         asyncio.ensure_future(c)
#         for c in islice(coros, 0, limit)
#     ]
#     async def first_to_finish():
#         # Wait until something finishes.
#         # Remove it from futures.
#         # Add a new task to futures.
#         # Return the finished one.

#         while len(futures) > 0:
#             yield first_to_finish()
# asyncio.run(print_when_done(coros))
