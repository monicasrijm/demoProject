from fastapi import FastAPI  # class-FastAPI

app = FastAPI()  # object

# CRUD APIs
# C - Create(Post)
# R - Read(Get)
# U - Update(Put/patch)
# D - Delete(Delete)
# fastapi run api in parallel way unlike flask and django


@app.get("/")
async def root():  # async-run function parallely
    return "This is home page"


@app.get("/sub")
async def subPage():
    return "This is sub home page"

"""
ORM-Object Relationship Manager - used to connect databases ,Eg : sqlalchemy
"""
# https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_7hz2t19t5c_e&adgrpid=155259815513&hvpone=&hvptwo=&hvadid=674842289437&hvpos=&hvnetw=g&hvrand=5520046121830359561&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9148884&hvtargid=kwd-10573980&hydadcr=14453_2316415&gad_source=1
