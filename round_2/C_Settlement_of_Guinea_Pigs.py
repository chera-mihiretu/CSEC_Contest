from sys import stdin,stdout
from math import ceil
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    nums = [int(i) for i in input().split()]
    before_doc = 0
    after_doc = 0
    answer = 0
    for i in range(n):
        if nums[i] == 1:
            before_doc += 1
        else:
            after_doc += before_doc
            before_doc = 0
        if after_doc & 1 or after_doc == 0:
            answer = max(answer, ceil(after_doc / 2) + before_doc)
        else:
            answer = max(answer, ceil((after_doc + 1) / 2) + before_doc)

    print(answer)


# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()