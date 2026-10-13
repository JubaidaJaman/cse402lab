 # FIFO Page Replacement Algorithm

frame_size = int(input("Enter frame size: "))

n = int(input("Enter number of pages: "))

pages = []

for i in range(n):
    page = int(input(f"Enter page {i + 1}: "))
    pages.append(page)

frames = []
page_faults = 0
page_hits = 0

print("
Page	Frames		Status")

for page in pages:

    if page in frames:
        page_hits += 1
        status = "Hit"

    else:
        page_faults += 1

        if len(frames) < frame_size:
            frames.append(page)
        else:
            frames.pop(0)
            frames.append(page)

        status = "Fault"

    print(page, "	", frames, "	", status)


# Calculate ratio
hit_ratio = page_hits / n
fault_ratio = page_faults / n

print("
Total Page Faults =", page_faults)
print("Total Page Hits =", page_hits)
print("Page Hit Ratio =", hit_ratio)
print("Page Fault Ratio =", fault_ratio)

