def is_safe(lev):
    is_inc = all(lev[i] < lev[i+1] for i in range(len(lev)-1))
    is_dec = all(lev[i] > lev[i+1] for i in range(len(lev)-1))

    if not (is_inc or is_dec):
        return False
    
    for i in range(len(lev) - 1):
        diff = abs(lev[i] - lev[i + 1])
        if diff < 1 or diff > 3:
            return False
    
    return True

def safe_by_rem(lev):
    for i in range(len(lev)):
        new_lev = lev[:i] + lev[i+1:]
        if is_safe(new_lev):
            return True
    return False

with open('input.txt', 'r') as file:
    reports = file.readlines()


# Part 1
safe_count = 0
for lines in reports:
    line = lines.strip()
    levels = list(map(int, line.split()))
    if is_safe(levels):
        safe_count += 1
print("Part 1 Safe: ", safe_count)


# Part 2
safe_count = 0
for lines in reports:
    line = lines.strip()
    levels = list(map(int, line.split()))
    if safe_by_rem(levels):
        safe_count += 1

print("Part 2 Safe: ", safe_count)
