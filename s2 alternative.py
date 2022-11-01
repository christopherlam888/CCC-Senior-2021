M, N, K = int(input()), int(input()), int(input())
canvas = []
for i in range(M*N):
    canvas.append(1)
for i in range(K):
    choice = input().split(" ")
    if choice[0] == "R":
        for j in range((int(choice[1])-1)*N, int(choice[1])*N):
            canvas[j] += 1
    elif choice[0] == "C":
        for j in range((int(choice[1])-1), M*N, N):
            canvas[j] += 1
gold = 0
for i in range(M*N):
    if canvas[i] % 2 == 0:
        gold += 1
print(gold)
