import networkx as nx
from datetime import datetime

def analyze_transaction(graph, transactions):
    risk_score = 0
    reasons = []
    
    cycles = list(nx.simple_cycles(graph))
    if cycles:
        risk_score += 0.5
        reasons.append("Cycle detected")
    
    sender_times = [datetime.strptime(t[2], "%Y-%m-%d %H:%M") 
                    for t in transactions if t[0] == transactions[0][0]]
    gaps = []
    for i in range(1, len(sender_times)):
        diff = (sender_times[i] - sender_times[i-1]).seconds / 60
        gaps.append(diff)
    
    if gaps and any(gap < 10 for gap in gaps):
        risk_score += 0.3
        reasons.append("High velocity detected")
    
    receivers = [t[1] for t in transactions if t[0] == transactions[0][0]]
    if len(set(receivers)) > 3:
        risk_score += 0.2
        reasons.append("Fan-out detected")
    
    return risk_score, reasons
