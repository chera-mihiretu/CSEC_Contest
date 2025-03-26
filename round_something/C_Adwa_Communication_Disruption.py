from sys import stdin
from heapq import *
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    s1 = list(input())
    s2 = list(input())
    diff = len(s1)
    blocked = [False  for _ in range(len(s1))]

    mm = {1 : s1, 2 : s2}

    for i in range(len(s1)):
        if s1[i] == s2[i]:
            blocked[i] = True
            diff -= 1
        

    t, q = [int(i) for i in input().split()]
    heap = []

    # print(s1, s2)
    for i in range(q):
        commands = [int(i) for i in input().split()]
        while heap and (i - heap[0][0] ) >= t:
            _, index = heappop(heap)
            if s1[index] != s2[index]:
                diff += 1
                blocked[index] = False


        if commands[0] == 1:
           i1 = commands[1] - 1
           if s1[i1] != s2[i1]:
                heappush(heap, (i, i1))
                blocked[commands[1]] = True
                diff -= 1

        if commands[0] == 2:
            _s1, _s2 = commands[1], commands[3]
            i1, i2 = commands[2] - 1, commands[4] - 1
            mm[_s1][i1], mm[_s2][i2] = mm[_s2][i2], mm[_s1][i1]

            if s1[i1] == s2[i1] and not blocked[i1]:
                blocked[i1] = True
                diff -= 1
            
            if s1[i1] != s2[i1] and blocked[i1]:
                blocked[i1] = False
                diff += 1

            
            if s1[i2] == s2[i2] and not blocked[i2]:
                blocked[i2] = True
                diff -= 1
            
            if s1[i2] != s2[i2] and blocked[i2]:
                blocked[i2] = False
                diff += 1


            
                    
        if commands[0] == 3:
            print("YES" if diff == 0 else "NO")
            



# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()