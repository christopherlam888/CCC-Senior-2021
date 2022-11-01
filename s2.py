M, N, K = int(input()), int(input()), int(input())
canvas = []
for i in range(M):
    canvas.append([1])
    for j in range(N-1):
        canvas[i].append(1)
for i in range(K):
    choice = (input().split(" "))
    if choice[0] == "R":
        for j in range(N):
            canvas[int(choice[1])-1][j] += 1
    elif choice[0] == "C":
        for j in range(M):
            canvas[j][int(choice[1])-1] += 1
gold = 0
for i in range(M):
    for j in range(N):
        if canvas[i][j] % 2 == 0:
            gold += 1
print(gold)
