
def solution():
    matrix = [[1,2,-1],[4,-1,6],[7,8,9]]
    result = []
    for i in range(len(matrix[0])):
        temp = []
        for j in range(len(matrix)):
            temp.append(matrix[j][i])
        result.append(temp)
    for i in range(len(result)):
        for j in range(len(result[0])):
            if result[i][j] == -1:
                result[i][j] == max(result[i])
    result_final = []
    for i in range(len(result[0])):
        temp = []
        for j in range(len(result)):
            temp.append(result[j][i])
        result_final.append(temp)
    return result_final

print(solution())