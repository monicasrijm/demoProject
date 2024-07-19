from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Home page"}


def majority(values):
    count = {}
    for element in values:
        if element in count:
            count[element] += 1
        else:
            count[element] = 1
    result = None
    for key, freq in count.items():
        if freq > len(values) // 2:
            result = key
            break
    return {"result": result}


@app.get("/numbers")
async def sub(numbers: str):
    values = numbers.replace(",", "")
    res = majority(values)
    if res["result"] is None:
        raise HTTPException(
            status_code=404, detail="No majority element found")
    return res


@app.post("/sub")
async def sub_post(numbers: str):
    values = numbers.replace(",", "")
    res = majority(values)
    if res["result"] is None:
        raise HTTPException(
            status_code=404, detail="No majority element found")
    return res
