from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Transaction(BaseModel):
    sender: str
    receiver: str
    amount: float
    timestamp: str
