from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    nums = [int(i) for i in input().split()]

    s = set(nums)

    l = list(s)
    l.sort()

    start, end = 0, len(l) - 1
    prev = -1
    while start < end:
        if  prev == -1:
            prev = l[start] * l[end]
        else:
            if prev != l[start] * l[end]:
                print('NO')
                break
        start += 1
        end -= 1
    
    print("YES")
# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()