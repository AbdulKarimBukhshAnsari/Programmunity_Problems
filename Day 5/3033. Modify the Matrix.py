class Solution(object):
    def modifiedMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        max_elements = []
        for i in range(len(matrix[0])):
            max_element = 0
            for j in range(len(matrix)):
                max_element = max(matrix[j][i], max_element)
            max_elements.append(max_element)
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                if matrix[j][i] == -1:
                    matrix[j][i] = max_elements[i]
        return matrix
        