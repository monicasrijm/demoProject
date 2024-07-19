from fastapi import FastAPI  # class-FastAPI

app = FastAPI()

new_dict = {
    "key1": "v1",
    "key2": "v2",
    1: "v3"
}


@app.get("/")
async def root():
    return new_dict


@app.get("/sub/fixed")
async def subpage():
    return "page fixed"


@app.get("/sub/{sub_page}")
async def subpage(sub_page: int):
    return new_dict.get(sub_page)
