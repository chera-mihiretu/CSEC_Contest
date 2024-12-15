from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    child = [0] * (n + 1)
    parent = list(range(n + 1))
    disrespect = [0] * (n + 1)
    child_dis = [0] * (n + 1)
    for i in range(1, n + 1):
        p, d = [int(i) for i in input().split()]
        if p != -1:
            child[p] += 1
        parent[i] = p
        disrespect[i] = d
    for i in range(1, n + 1):
        child_dis[parent[i]] += disrespect[i]
    answer = []
    for i in range(1, n + 1):
        if disrespect[i] == 1:
            if child[i] == child_dis[i]:
                answer.append(i)
    # print(child, child_dis)
    if not answer:
        print(-1)
    else:
        print(*answer)

# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()