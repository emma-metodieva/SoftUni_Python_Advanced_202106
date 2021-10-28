from os import walk

_, _, files = next(walk(input()))

by_ext = {}

for file in files:
    ext = file.split('.')[-1]
    if ext not in by_ext:
        by_ext[ext] = []
    by_ext[ext].append(file)

with open("report.txt", 'w') as file:
    for ext in sorted(by_ext.keys()):
        files = sorted(by_ext[ext])
        file.write(f".{ext}\n")

        for f in files:
            file.write(f"---{f}\n")
