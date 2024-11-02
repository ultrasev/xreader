#!/usr/bin/env python3
from abc import ABC, abstractmethod
import httpx
import re
import asyncio
from loguru import logger
from .types import AbstractReader


class JinaReader(AbstractReader):
    def __init__(self):
        self.endpoint = "https://r.jina.ai/"

    async def scrape(self, url: str) -> str:
        try:
            async with httpx.AsyncClient(timeout=30) as client:
                response = await client.get(f"{self.endpoint}{url}")
                if response.status_code == 200:
                    content = response.text
                    if content.strip():
                        logger.info(
                            f"Jina API returned content: {content}")
                        return content
                    logger.warning("Jina API returned empty content")
                else:
                    logger.error(
                        f"Jina API failed with status code: {response.status_code}, text: {response.text}")
                return ""
        except Exception as e:
            logger.error(f"Jina API failed: {e}")
            return ""


class JinaTweetReader(JinaReader):
    def is_content_valid(self, content: str, username: str) -> bool:
        if username in content or 'Conversation' in content:
            return True
        if '---' in content:
            return True
        if 'Title: X' not in content:
            return True
        return False

    async def reads(self, url: str) -> str:
        pattern = r'(?:x\.com|twitter\.com)/([\w\.]+)/status/(\d+)'
        match = re.search(pattern, url)
        if not match:
            logger.warning(f"Invalid tweet URL format: {url}")
            return ""
        username = f"@{match.group(1)}"
        logger.info(f"username: {username}")
        for retry in range(5):
            content = await self.scrape(url)
            content = content.replace("\\", "")
            if self.is_content_valid(content, username):
                return content
            logger.warning(f"content for {url} is not valid, retrying...")
            await asyncio.sleep(1 << (retry + 2))
        return ""
