def shiftGrid() -> list[list[int]]:
    k=4
    grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
    grid_d = [grid[i][j] for i in range(len(grid)) for j in range(len(grid[0]))]
    result = [0 for i in range(len(grid_d))]
    for i in range(len(result)):
        result[(k+i)%len(result)] =  grid_d[i]
    final_result = []
    n = 0 
    for i in range(len(grid)):
        temp = []
        for j in range(len(grid[0])):
            temp.append(result[n])
            n+=1
        final_result.append(temp)
    return final_result 

print(shiftGrid())