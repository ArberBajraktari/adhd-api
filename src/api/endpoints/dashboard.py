from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/")
async def home (request: Request):
    return {"status": "on construction like an animal"}