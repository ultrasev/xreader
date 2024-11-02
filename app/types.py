from pydantic import BaseModel, HttpUrl, validator
import re
from .exceptions import TwitterAPIException


class TwitterURL(BaseModel):
    url: HttpUrl

    @validator('url', pre=True)
    def format_url(cls, v):
        if isinstance(v, str):
            v = v.strip()
            if v.startswith(('http://', 'https://')):
                return v
            return f"https://{v}"
        return v

    @validator('url')
    def validate_twitter_url(cls, v):
        url_str = str(v)
        pattern = r'^https?://(?:www\.)?(twitter|x)\.com/\w+/status/\d+$'
        if not re.match(pattern, url_str):
            raise TwitterAPIException(
                'Invalid Twitter URL format. Must be like: https://twitter.com/username/status/123456789'
            )
        return url_str
