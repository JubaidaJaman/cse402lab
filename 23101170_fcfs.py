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

process.sort(key=lambda x: x.at)

current_time = 0
for p in process:
    if current_time < p.at:
        current_time = p.at
    p.ct = current_time + p.bt
    p.tat = p.ct - p.at
    p.wt = p.tat - p.bt
    current_time = p.ct

print("\nPID\tAT\tBT\tCT\tTAT\tWT")
for p in sorted(process, key=lambda x: x.pid):
    print(f"{p.pid}\t{p.at}\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}")

avg_tat = sum(p.tat for p in process) / n
avg_wt = sum(p.wt for p in process) / n

print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
print(f"Average Waiting Time:    {avg_wt:.2f}")
