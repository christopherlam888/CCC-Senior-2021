N = int(input())
if N == 1:
    print(0)
else:
    friends = []
    positions = []
    for i in range(N):
        components = input().split(" ")
        friends.append([int(components[0]), int(components[1]), int(components[2])])
        positions.append(int(components[0]))
    total_times = []
    for i in range(min(positions), max(positions)):
        total_time = 0
        for j in range(N):
            distance = abs(i - friends[j][0])
            if i == friends[j][0] or distance <= friends[j][2]:
                total_time += 0
            else:
                total_time += (distance-friends[j][2])*friends[j][1]
        total_times.append(total_time)
    print(min(total_times))
