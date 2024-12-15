from sys import stdin,stdout
from math import ceil
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n,k = [int(i) for i in input().split()]

    """
    1 3 5 7 9 2 4 6 8 10
    1 2 3 4 5 6 7 8 9 10

    1 3 5 2 4 
    
    7 / 2 -> 4
    1 3 5 7 
    1 -> 1
    2 -> 3
    3 -> 5
    
    2 4 6

    1 -> 2
    2 -> 4
    3 -> 6

    """

    if k <= ceil(n/2):
        print(2*k - 1)
    else:
        print(2 * (k - ceil(n/2)))


# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()