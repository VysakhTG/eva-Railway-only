import os
import aiohttp
from requests.utils import requote_uri

API_1337x = "https://api.abir-hasan.tk/1337x?query={}&limit={}"
API_YTS = "https://api.abir-hasan.tk/yts?query={}&limit={}"
API_PIRATEBAY = "https://api.abir-hasan.tk/piratebay?query={}&limit={}"
API_ANIME = "https://api.abir-hasan.tk/anime?query={}&limit={}"
MAX_INLINE_RESULTS = int(os.environ.get("MAX_INLINE_RESULTS", 50))

async def Search1337x(query: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(requote_uri(API_1337x.format(query, MAX_INLINE_RESULTS))) as res:
            return (await res.json())["results"] if ((await res.json()).get("results", None) is not None) else [] 

async def SearchYTS(query: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(requote_uri(API_YTS.format(query, MAX_INLINE_RESULTS))) as res:
            return (await res.json())["results"] if ((await res.json()).get("results", None) is not None) else []

async def SearchPirateBay(query: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(requote_uri(API_PIRATEBAY.format(query, MAX_INLINE_RESULTS))) as res:
            return (await res.json())["results"] if ((await res.json()).get("results", None) is not None) else []


async def SearchAnime(query: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(requote_uri(API_ANIME.format(query, MAX_INLINE_RESULTS))) as res:
            return (await res.json())["results"] if ((await res.json()).get("results", None) is not None) else []
