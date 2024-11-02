#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import List


class AbstractReader(ABC):
    @abstractmethod
    async def reads(self, url: str) -> str:
        pass

    def __or__(self, other: 'AbstractReader') -> 'AbstractReader':
        return ConcatReader([self, other])


class ConcatReader(AbstractReader):
    def __init__(self, readers: List[AbstractReader]):
        self.readers = readers

    async def reads(self, url: str) -> str:
        contents = []
        for reader in self.readers:
            content = await reader.reads(url)
            contents.append(content)
            if content:
                return content
        return max(contents, key=len)
