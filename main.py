from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Transaction(BaseModel):
    sender: str
    receiver: str
    amount: float
    timestamp: str


import networkx as nx
from detection_engine import analyze_transaction

G = nx.DiGraph()
transactions = []

@app.post("/analyze-transaction")
def analyze(transaction: Transaction):
    G.add_edge(transaction.sender, transaction.receiver, 
               amount=transaction.amount, 
               timestamp=transaction.timestamp)
    transactions.append((transaction.sender, transaction.receiver, transaction.timestamp))
    score, reasons = analyze_transaction(G, transactions)
    return {"risk_score": score, "reasons": reasons}
