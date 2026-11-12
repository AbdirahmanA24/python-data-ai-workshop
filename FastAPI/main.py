from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"Message": "Hello"}

airports = ["KMSP", "KJFK"]

@app.get("/airports")
def get_airports():
    return {"airports": airports}

@app.post("/airports")
def add_airport(code: str):
    airports.append(code)
    return {"message": "Aiport added"}

@app.put("/airports/{index}")
def update_airports(code: str, index: int):
    airports[index] = code
    return {"message": "airport updated"}

@app.delete("/airports/{index}")
def pop_airport(index: int):
    airports.pop(index)
    return {"message": "Airport updated"}