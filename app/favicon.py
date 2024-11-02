from fastapi.responses import Response
from fastapi import APIRouter
system_router = APIRouter(
    prefix="",
    tags=["system"],
    include_in_schema=False
)


async def get_favicon():
    # Simple 16x16 transparent ICO file in bytes
    favicon_bytes = bytes([
        0x00, 0x00, 0x01, 0x00, 0x01, 0x00, 0x10, 0x10,
        0x00, 0x00, 0x01, 0x00, 0x20, 0x00, 0x68, 0x04,
        0x00, 0x00, 0x16, 0x00, 0x00, 0x00
    ] + [0x00] * 1024)  # Padding with zeros for transparency

    return Response(
        content=favicon_bytes,
        media_type="image/x-icon"
    )


@system_router.get("/favicon.ico")
async def favicon():
    return await get_favicon()
