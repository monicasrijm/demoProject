from fastapi import FastAPI  # class-FastAPI

app = FastAPI()

new_dict = {
    "key1": "v1",
    "key2": "v2",
    1: "v3",
    5: "this"
}


@app.get("/")
async def root():
    return new_dict


@app.get("/sub")
# query can be used to give and change value dynamically
async def subpage(sub_page: int | None, query: bool | None = None):
    if query:
        return "Yes"
    else:
        return new_dict.get(sub_page)
