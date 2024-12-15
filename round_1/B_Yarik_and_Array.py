from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    nums = [int(i) for i in input().split()]
    current_sum = nums[0]
    max_sum = nums[0]
    for i in range(1, n):
        current_sum = max(nums[i], current_sum + nums[i])
        if nums[i] % 2 == nums[i-1] % 2:
            current_sum = nums[i]
        max_sum = max(max_sum, current_sum)
    print(max_sum)
# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()