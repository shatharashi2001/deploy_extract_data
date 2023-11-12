from fastapi import FastAPI
import uvicorn
from router import router
from errors import *


app = FastAPI()
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")
