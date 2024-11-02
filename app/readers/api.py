import httpx
from aiocache import cached
from loguru import logger

from .jina import JinaTweetReader
from .types import AbstractReader
from .cache import cached


class InitReader(AbstractReader):
    """ Reader initializer, warms up the jina.ai API endpoint
    """

    async def reads(self, url: str) -> str:
        async with httpx.AsyncClient(timeout=30) as client:
            await client.get(f'https://r.jina.ai/{url}')
            return ''


class ReactTweetReader(AbstractReader):
    async def reads(self, url: str) -> str:
        try:
            tweet_id = url.split('/')[-1]
            api_url = f"https://react-tweet.vercel.app/api/tweet/{tweet_id}"
            logger.info(f"React-tweet API URL: {api_url}")

            async with httpx.AsyncClient(timeout=30) as client:
                response = await client.get(api_url)
                if response.status_code == 200:
                    data = response.json()
                    if 'data' in data and 'text' in data['data']:
                        logger.info(
                            f"React-tweet API returned content: {data['data']['text']}"
                        )
                        text = data['data']['text']
                        if '…' in text:
                            logger.warning(
                                "React-tweet API returned truncated content")
                            return ""
                        return text
                    logger.warning(
                        "React-tweet API response missing text field")
                else:
                    logger.error(
                        f"React-tweet API failed with status code: {response.status_code}"
                    )
                return ""
        except Exception as e:
            logger.error(f"React-tweet API failed: {e}")
            return ""


class TwitterReader(AbstractReader):
    def __init__(self):
        self.reader = InitReader() | ReactTweetReader() | JinaTweetReader()

    async def reads(self, url: str) -> str:
        return await self.reader.reads(url)


reader = TwitterReader()


@cached(ttl=86400)
async def reads(url: str) -> str:
    url = url.replace("/twitter.com/", "/x.com/")  # to avoid 308 redirect
    return await reader.reads(url)
