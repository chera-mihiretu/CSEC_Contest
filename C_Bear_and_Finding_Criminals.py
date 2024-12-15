from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution


def solution():
    n, k  = [int(i) for i in input().split()]
    nums = [int(i) for i in input().split()]
    start  = end = k -1
    l = r = 0
    ll  = None
    while start != 0 and end != n - 1:
        l += nums[start]
        r += nums[end]
        if nums[end] != 0:
            if ll == None:
                ll = False
        if nums[start] != 0:
            if ll == None:
                ll = True

        nums[start] = 0
        if start != 0:
            start -= 1
        nums[end] = 0
        if r != n - 1:
            r += 1
    if ll:
        print(l)
    else:
        print(r)
        
# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()