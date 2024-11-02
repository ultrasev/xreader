from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse, HTMLResponse
from .exceptions import TwitterAPIException
from .types import TwitterURL
from .readers import reads
from .html import HTML_CONTENT

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def root():
    return HTMLResponse(content=HTML_CONTENT, status_code=200)


@router.get("/{url:path}")
async def x(url: str):
    try:
        twitter_url = TwitterURL(url=url)
        text = await reads(twitter_url.url)
        return JSONResponse(status_code=200, content={"text": text, "status": "success"})
    except TwitterAPIException as e:
        return JSONResponse(status_code=e.status_code, content={"message": e.detail, "status": "Invalid URL"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e), "status": "Internal Server Error"})
