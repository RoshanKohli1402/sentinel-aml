import networkx as nx
G = nx.DiGraph()
G.add_edge("A", "B", amount=10000, timestamp="2026-04-01 10:00")
G.add_edge("B", "C", amount=10000, timestamp="2026-04-01 10:03")
G.add_edge("C", "D", amount=10000, timestamp="2026-04-01 10:05")
G.add_edge("D", "E", amount=10000, timestamp="2026-04-01 10:09")
G.add_edge("E", "A", amount=10000, timestamp="2026-04-01 10:12")

print(list(nx.simple_cycles(G)))

if list(nx.simple_cycles(G)):
  print("ALERT: Cycle detected - possible money laundering")
else:
  print("No cycle found")

rom datetime import datetime

transactions = [
    ("A", "B", "2026-04-01 10:00"),
    ("A", "C", "2026-04-01 10:02"),
    ("A", "D", "2026-04-01 10:04"),
    ("A", "E", "2026-04-01 10:06"),
]

times = [datetime.strptime(t[2], "%Y-%m-%d %H:%M") for t in transactions]


gaps = []
for i in range(1, len(times)):
    diff = (times[i] - times[i-1]).seconds / 60
    gaps.append(diff)

print(gaps)


if any(gap < 10 for gap in gaps):
    print("ALERT: High velocity detected - rapid transfers from same account")
else:
    print("No velocity issue")

count = 0
for b in transactions:
  if b[0] == 'A':
    count += 1
print(count)
if count > 3:
  print("ALERT: Fan- Out alert - rapid transfers from same account")
else:
  print("No  issue")


def analyze_transaction(graph, transactions):
    risk_score = 0
    reasons = []
    
    cycles = list(nx.simple_cycles(graph))

    if cycles:
        risk_score +=  0.5
        reasons.append("Cycle detected")

    if  any(gap < 10 for gap in gaps):
      risk_score += 0.3
      reasons.append("High velocity detected")

    if count > 3:
      risk_score += 0.2
      reasons.append("Fan- Out alert")

    return risk_score, reasons

score, reasons = analyze_transaction(G, transactions)
print("Risk Score:", score)
print("Reasons:", reasons)
