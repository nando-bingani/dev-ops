from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": " World from self-hosted actions! continue testing-backend"}
