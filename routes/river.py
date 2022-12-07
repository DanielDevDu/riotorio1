from fastapi import APIRouter, Depends, HTTPException, status

river_router = APIRouter(
    prefix="/river",
    tags=["River"],
)

@river_router.get("/")
def river():
    return {"message": "In River Route"}