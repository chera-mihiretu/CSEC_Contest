from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    nums = [int(i) for i in input().split()]
    nums[0] += 1
    for i in range(1, n):
        if nums[i] == 1:
            nums[i] += 1
        if not nums[i] % nums[i-1]:
            nums[i] += 1
        
    print(*nums)


# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()