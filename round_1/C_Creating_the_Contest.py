from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    nums = [int(i) for i in input().split()]
    count = 1
    answer= 1 
    for i in range(1, n):
        if nums[i] <= nums[i-1] * 2:
            count += 1
        else:
            count = 1
        answer = max(answer, count)
    print(answer)

# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()