from fastapi import HTTPException
from typing import Optional


class TwitterAPIException(HTTPException):
    def __init__(
        self,
        message: str,
        status_code: int = 400,
        headers: Optional[dict] = None
    ):
        super().__init__(
            status_code=status_code,
            detail={"message": message},
            headers=headers
        )
