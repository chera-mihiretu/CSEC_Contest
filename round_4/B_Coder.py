from sys import stdin,stdout
from math import ceil
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())

    answer  = [['.' for _ in range(n)] for i in range(n)]
   
    for i in range(n):
        for j in range(n):
            if i & 1 == 0 and j & 1 == 0:
                answer[i][j] = 'C'


            if j & 1 == 1 and i & 1 == 1:
                answer[i][j] = 'C'
    res = (n // 2) * n
    if n & 1 == 1:
        res += ceil(n / 2)
    print(res)
    for i in answer:
        print(*i, sep="")
    


# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()