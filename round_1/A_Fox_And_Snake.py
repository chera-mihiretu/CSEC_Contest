from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n,m = [int(i) for i in input().split()]
    answer = [['.' for i in range(m)] for i in range(n)]
    for i in range(0,n, 2):
        for j in range(m):
            answer[i][j] = '#'
    odd = 0
    for i in range(1, n, 2):
        if odd % 2:
            answer[i][0] = '#'

        else:
            answer[i][-1] = '#'
        odd += 1

    for row in answer:
        print(*row, sep='')


# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()