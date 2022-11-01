N, heights, widths = int(input()), input().split(" "), input().split(" ")
height_differences = []
for i in range(N):
    height_differences.append(abs(int(heights[i])-int(heights[i+1])))
area = 0
for i in range(N):
    area += min(int(heights[i]), int(heights[i+1]))*int(widths[i]) + (int(widths[i])*int(height_differences[i]))/2
print(area)
