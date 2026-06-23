from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def get_users(page: int = 1):
    return {
        "page": page
    }
