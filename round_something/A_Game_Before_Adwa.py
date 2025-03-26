from sys import stdin,stdout
from collections import Counter
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n,k = [int(i) for i in input().split()]
    nums = [int(i) for i in input().split()]
    nums.sort()

    left = 0
    right = n - 1
    answer = 0
    while left < right:
        if nums[left] + nums[right] < k:
            left += 1
        elif nums[left] + nums[right] > k:
            right -= 1
        else:
            right -= 1
            left += 1
            answer +=1 
    print(answer)
            
        

    

    

# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()