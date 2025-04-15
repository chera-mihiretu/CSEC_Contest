from sys import stdin,stdout
from bisect import bisect_left
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n, k, q = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]

    pref = [0] * (k)
    pref[0] = a[0]
    for i in range(1, k):
        pref[i] = pref[i-1] + a[i]
    

    speed = [0] * (k)
    for i in range(k):
        if i == 0:
            speed[i] = (b[i] - 0) / (a[0] - 0)
        else:
            print(a[i], a[i-1], b[i], b[i-1])
            speed[i] = (b[i] - b[i-1]) / (a[i] - a[i-1])


    pref_dis = [0] * (k)
    pref_dis[0] = a[0]
    for i in range(1, k):
        pref_dis[i] = pref_dis[i-1] + a[i]
    
    for _ in range(q):
        x = int(input())

        i = bisect_left(pref_dis, x)

        print(a[i] + ((i - a[i]) * speed[i + 1]))



# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()