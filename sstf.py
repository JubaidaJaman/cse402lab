 # SSTF Disk Scheduling

head = int(input("Enter initial head position: "))

n = int(input("Enter number of requests: "))

requests = []

for i in range(n):
    x = int(input(f"Enter request {i + 1}: "))
    requests.append(x)

total = 0
current = head

print("
SSTF Sequence:")

while requests:


    nearest = min(requests, key=lambda x: abs(x - current))

    movement = abs(nearest - current)

    print(current, "->", nearest, "=", movement)

    total += movement
    current = nearest

    requests.remove(nearest)

print("
Total Seek Operations =", total)
