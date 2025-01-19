from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    nums = [int(i) for i in input().split()]

    while len(nums) > 1:
        if abs(nums[-1] - nums[-2]) <= 1:
            nums.pop()
        else:
            break
    if len(nums) == 1:
        print('YES')
    else:
        print("NO")



# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()