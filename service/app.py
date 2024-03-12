"""
Simple FastAPI app
"""

from fastapi import FastAPI
import os

message = os.environ.get("SERVER_MESSAGE", "World")

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": message}
