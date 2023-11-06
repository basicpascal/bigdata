n = int(input())
usernames = {}
results = []

for _ in range(n):
    name = input()
    if name in usernames:
        i = 1
        while f"{name}{i}" in usernames:
            i += 1
        new_name = f"{name}{i}"
        usernames[new_name] = True
        results.append(new_name)
    else:
        usernames[name] = True
        results.append("OK")

for result in results:
    print(result)
