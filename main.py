from fastapi import FastAPI
from api.helloworldRouter import router

app = FastAPI()

app.include_router(router)
