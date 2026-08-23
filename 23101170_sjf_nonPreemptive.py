class Process:
    def __init__(self, pid, at, bt):
        self.pid, self.at, self.bt = pid, at, bt
        self.ct = self.tat = self.wt = 0


n = int(input("Enter number of processes: "))
process = []

for i in range(n):
    pid = f"p{i+1}"
    at = int(input(f"Enter Arrival Time for {pid}: "))
    bt = int(input(f"Enter Burst Time for {pid}: "))
    process.append(Process(pid, at, bt))

completed = []
unvisited = process.copy()
time = 0

while unvisited:
    ready = [p for p in unvisited if p.at <= time]
    if not ready:
        time += 1
        continue
    curr = min(ready, key=lambda p: p.bt)
    time += curr.bt
    curr.ct = time
    curr.tat = curr.ct - curr.at
    curr.wt = curr.tat - curr.bt
    completed.append(curr)
    unvisited.remove(curr)

print("\nPID\tAT\tBT\tCT\tTAT\tWT")
for p in sorted(completed, key=lambda x: x.pid):
    print(f"{p.pid}\t{p.at}\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}")

avg_tat = sum(p.tat for p in completed) / n
avg_wt = sum(p.wt for p in completed) / n

print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
print(f"Average Waiting Time:    {avg_wt:.2f}")
