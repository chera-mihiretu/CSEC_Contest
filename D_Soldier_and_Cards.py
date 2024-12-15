from sys import stdin,stdout
from collections import deque
from collections import Counter
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    first = deque([int(i) for i in input().split()][1:])
    second = deque([int(i) for i in input().split()][1:])

    left_count = Counter()
    right_count = Counter()
    steps = 0
    while first and second:
        if steps >= 100000:
            break
        top_l = first.popleft()
        top_r = second.popleft()

        if top_l > top_r:

            first.append(top_r)
            first.append(top_l)
        else:
            second.append(top_l)
            second.append(top_r)
        

        steps += 1
    else:
        if first:
            return [steps, 1]
        else:
            return [steps, 2]
    return [-1]
# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        print(*solution())