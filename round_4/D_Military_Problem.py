
import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    n, q = [int(i) for i in input().split()]
    graph = [[] for i in range(n)]
    edges = [int(i) for i in input().split()]
    child_count = [0 for i in range(n)]
    for i in range(len(edges)):
        graph[i + 1].append(edges[i]-1)
        graph[edges[i]-1].append(i + 1)
    for i in range(len(graph)):
        graph[i].sort()
    
    answer = []

    def dfs(graph, node, parent):
        nonlocal answer
        answer.append(node)
        children = 1
        for child in graph[node]:
            if child != parent:
                children += dfs(graph, child, node)
        child_count[node] = children
        return children
    dfs(graph, 0, -1)


    m = {}
    for i in range(len(answer)):
        m[answer[i]] = i
    result = [-1 for i in range(q)]
    # print(answer)
    for i in range(q):
        u, k = [int(i) - 1 for i in input().split()]
        start_index = m[u]
        end_k = start_index + k 
        
        if k < child_count[u]:
            result[i] = answer[end_k] + 1
    
    print(*result, sep="\n")
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
