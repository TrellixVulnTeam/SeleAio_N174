# import aiohttp, asyncio, async_timeout
# from zmq import Stopwatch

# async def urlGetCOROUTINE( aSESSION, anURL2GET, aCoroID = -1, anAsyncTIMEOUT = 10 ):
#     aLocalCLK = Stopwatch()
#     res       = ""
#     ############################################# SECTION-UNDER-TEST
#     aLocalCLK.start() ##############################################
#     with async_timeout.timeout( anAsyncTIMEOUT ):# RESPONSE ######## TIMEOUT-PROTECTED
#          async  with aSESSION.get( anURL2GET ) as aRESPONSE:
#             while True:
#                     pass;  aGottenCHUNK = await   aRESPONSE.content.read( 1024 )
#                     if not aGottenCHUNK:
#                         break
#                     res += str( aGottenCHUNK )
#             await                                 aRESPONSE.release()
#     ################################################################ TIMEOUT-PROTECTED
#     aTestRunTIME_us = aLocalCLK.stop() ########## SECTION-UNDER-TEST

#     print( "Now finished urlGetCOROUTINE(launch_id:<{2: >2d}>) E2E execution took {0: >9d} [us](Safety anAsyncTIMEOUT was set {1: >2d} [s])".format( aTestRunTIME_us, anAsyncTIMEOUT, aCoroID ) )
#     return ( aTestRunTIME_us, len( res ) )

# async def mainAsyncLoopPAYLOAD_wrapper( anAsyncLOOP_to_USE, aNumOfTESTs = 10, anUrl2GoGET = "http://example.com" ):
#     '''
#     aListOfURLs2GET = [ "https://www.irs.gov/pub/irs-pdf/f1040.pdf",
#                         "https://www.forexfactory.com/news",
#                          ...
#                          ]
#     '''
#     async with aiohttp.ClientSession( loop = anAsyncLOOP_to_USE ) as aSESSION:
#         aBlockOfAsyncCOROUTINEs_to_EXECUTE = [ urlGetCOROUTINE(      aSESSION, anUrl2GoGET, launchID ) for launchID in range( min( aNumOfTESTs, 1000 ) ) ]
#         await asyncio.gather( *aBlockOfAsyncCOROUTINEs_to_EXECUTE )
# asyncio.run(urlGetCOROUTINE())
