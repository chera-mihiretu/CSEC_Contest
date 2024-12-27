from sys import stdin,stdout
from collections import Counter
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())

    string = input()
    count = Counter()
    answer = 1
    for i in range(n - 2, -1, -1):
        answer += i + 1
        
        answer -= count[string[i]]
        count[string[i]] += 1
    print(answer) 


# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()