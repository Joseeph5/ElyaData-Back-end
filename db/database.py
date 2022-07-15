import motor.motor_asyncio
from models.blog import Blog
from settings import MONGO_URL
from bson import ObjectId

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db = client.ElyaDataBase


async def fetch_one_blog(title):
    return 1

async def fetch_all_blogs():
    posts = []
    documents = db.posts.find({})
    async for document in documents:
        posts.append(Blog(**document))
    return posts

async def create_blog(blog):
    document = blog
    result = await db.posts.insert_one(dict(blog))
    print('result',result.inserted_id)
    document.id = result.inserted_id
    return document

async def get_blog(id):
    document = await db.posts.find_one({"_id": ObjectId(id)})
    print('document',document)
    return Blog(**document)

async def put_blog(id:str,blog:Blog):
    result = await db.posts.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(blog),"$currentDate": {"lastModified": True}
    })
    blog.id = id
    return blog

async def remove_todo(id: str):
    await db.posts.find_one_and_delete({"_id": ObjectId(id)})
    return True