from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    
    n = int(input())
    nums = [int(i) for i in input().split()]
    curr = 0
    for i in range(1, len(nums)):
        if nums[curr] > nums[i]:
            curr = i
    if curr != 0:
        print("NO")
    else:
        print("YES")
# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()