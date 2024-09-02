class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        i = 0
        j = 0
        num = n - 1
        mode = 1
        k = 1
        matrix = [[0 for _ in  range(n)] for _ in range(n)]
        while mode <= 4:
            for _ in range(num):
                matrix[i][j] = k
                if mode == 1:
                    j += 1
                elif mode == 2:
                    i += 1
                elif mode == 3:
                    j -= 1
                elif mode == 4:
                    i -= 1
                k += 1
            if mode == 4:
                i += 1
                j += 1
                num -= 2 
                mode = 1
            else:
                mode += 1
            if num <= 0:
                if n %2 ==1:
                    matrix[n//2][n//2] = k
                    break
                else:
                    break
        return matrix
