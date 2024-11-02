#!/usr/bin/env python3
from fastapi import FastAPI, APIRouter
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from app.hello import router as hello_router
from app.x import router as x_router
from app.middleware import log_requests, CORS_CONFIG
from app.favicon import system_router

app = FastAPI()


app.include_router(system_router)
app.include_router(hello_router, prefix="/hello")
app.include_router(x_router, prefix="")
app.add_middleware(CORSMiddleware, **CORS_CONFIG)
app.middleware("http")(log_requests)


@app.get("/")
def _root():
    return Response(content=html, media_type="text/html")
