# Tristan Le 7/04/2024

file_name = input("Enter file:")

if len(file_name) < 1:
    file_name = "mbox-short.txt"

hours_count = {}
with open(file_name, "r") as file:
    for line in file:

        if line.startswith('From '):
            time = line.split()[5]
            hour = time.split(':')[0]
            hours_count[hour] = hours_count.get(hour, 0) + 1

for hour, count in sorted(hours_count.items()):
    print(hour, count)