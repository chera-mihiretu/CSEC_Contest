from sys import stdin,stdout
from heapq import * 
# take input
input = lambda: stdin.readline().strip()

# solution
def solution():
    n,m,k = [int(i) for i in input().split()]
    nums = [int(i) for i in input().split()]
    heap = [k for i in range(m)]
    count = 0
    for i in range(n):
        contain = heappop(heap)
        if contain - nums[i] < 0:
            heappush(heap, contain)
        else:
            heappush(heap, contain + nums[i])
            count +=1
    print(count)
               


    



# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()




















"""