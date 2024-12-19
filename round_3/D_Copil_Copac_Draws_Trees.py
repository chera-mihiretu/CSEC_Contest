from sys import stdin,stdout
from collections import deque
from collections import defaultdict
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    answer = [1] + [0] * (n - 1)
    edges = []
    que = deque()
    indexing = defaultdict(lambda: float('inf'))
    graph = [[] for i in range(n)]
    visited = [False for i in range(n)]
    for i in range(n-1):
        fr, to = [int(i) - 1 for i in input().split()]
        indexing[(min(fr, to), max(fr, to))] = i
        graph[fr].append(to)
        graph[to].append(fr)
    que = deque([(0, 0, -1)])
    answer = 0
    while que:
        
        node, step, parent = que.popleft()
        answer = max(step, answer)
        for child in graph[node]:
            if not visited[child]:
                if indexing[(min(node, parent), max(node, parent))] > indexing[(min(node, child), max(node, child))]:
                    que.append((child, step, node))
                else:
                    que.append((child, step + 1, node))
                visited[child] = True

    print(answer)
        



# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()