

from fastapi import FastAPI

app = FastAPI()



@app.get("/")
async def root():
    return {"m": "a"}

@app.get("/posts")
def get_posts():
    return {"a":"b"}
