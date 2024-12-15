from sys import stdin,stdout
from math import ceil
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    graph = [[] for i in range(n)]

    for i in range(n-1):
        fr, to = [int(i) for i in input().split()]
        graph[fr-1].append(to - 1)
        graph[to-1].append(fr - 1)
    answer = 0
    for i in graph:
        if len(i) == 1:
            answer += 1
    print(ceil(answer / 2))
        



# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()