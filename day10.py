n, k = map(int, input().split())
people = list(range(1, n + 1))
result = []
index = 0

for _ in range(n):
    for _ in range(k - 1):
        index = (index + 1) % len(people)
    result.append(people.pop(index))

print("<" + ", ".join(map(str, result)) + ">")
