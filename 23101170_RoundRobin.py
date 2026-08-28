from collections import deque

class Process:
    def __init__(self, pid, at, bt):
        self.pid, self.at, self.bt, self.rt = pid, at, bt, bt
        self.ct = self.tat = self.wt = 0

n = int(input("Enter number of processes: "))
process = []

for i in range(n):
    pid = f"p{i+1}"
    at = int(input(f"Enter Arrival Time for {pid}: "))
    bt = int(input(f"Enter Burst Time for {pid}: "))
    process.append(Process(pid, at, bt))

q = int(input("Enter the quantum: "))

time, done = 0, 0
queue = deque()
visited = set()

process.sort(key=lambda x: x.at)

for p in process:
    if p.at <= time:
        queue.append(p)
        visited.add(p)

while done < n:
    if not queue:
        time += 1
        for p in process:
            if p.at <= time and p not in visited:
                queue.append(p)
                visited.add(p)
        continue

    curr = queue.popleft()
    run_time_slice = min(q, curr.rt)
    curr.rt -= run_time_slice
    time += run_time_slice

    for p in process:
        if p.at <= time and p not in visited:
            queue.append(p)
            visited.add(p)

    if curr.rt > 0:
        queue.append(curr)
    else:
        curr.ct = time
        curr.tat = curr.ct - curr.at
        curr.wt = curr.tat - curr.bt
        done += 1

print("\nPID\tAT\tBT\tCT\tTAT\tWT")
for p in sorted(process, key=lambda x: x.pid):
    print(f"{p.pid}\t{p.at}\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}")

avg_tat = sum(p.tat for p in process) / n
avg_wt = sum(p.wt for p in process) / n

print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
print(f"Average Waiting Time:    {avg_wt:.2f}")
