from fastapi import APIRouter,HTTPException
from fastapi.encoders import jsonable_encoder

from db.database import (fetch_all_blogs,create_blog,get_blog,put_blog,remove_todo)
from models.blog import Blog

router = APIRouter(
    prefix="/blogs",
)

@router.get("/")
async def get_blogs():
    response = await fetch_all_blogs()
    return response

@router.post("/create", response_model=Blog)
async def insert_blog(blog:Blog):
    
    response = await create_blog(blog)
    if response:
       return response
    raise HTTPException(400, "Something went wrong")

@router.get("/{id}")
async def fetch_one_blog(id):
    response = await get_blog(id)
    if response :
       return response
    raise HTTPException(404, f"there is not blog with this id: {id}")

@router.put("/update/{id}/", response_model=Blog)
async def update_blog(id: str, blog: Blog):
    print('update_blog',blog)
    response = await put_blog(id, blog)
    if response:
        return response
    raise HTTPException(404, f"There is no blog with the id: {id}")

@router.delete("/{id}")
async def delete_blog(id:str):
    response = await remove_todo(id)
    if response:
        return {"message":"Successfully deleted blog"}
    raise HTTPException(404, f"There is no blog with the id: {id}")