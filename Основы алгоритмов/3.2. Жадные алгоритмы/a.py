n = int(input())
events = [tuple(map(int, input().split())) for _ in range(n)]
events.sort(key=lambda t: t[1])  # sort by the end

count = 0
while len(events):
    count += 1
    r = events[0][1]
    events.pop(0)

    while len(events) and events[0][0] <= r:
        events.pop(0)

print(count)
