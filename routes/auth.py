from fastapi import APIRouter, Depends, HTTPException, status

auth_router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

@auth_router.get("/")
def auth():
    return {"message": "In Auth"}