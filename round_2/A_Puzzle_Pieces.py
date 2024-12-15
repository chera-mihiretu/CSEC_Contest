from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    x, y = [int(i) for i in input().split()]
    x, y = min(x, y), max(x, y)

    if x == 1 or y == 1:
        print('YES')
    elif x > 2 and y == 1:
        print('YES')
    elif x == 2 and y == 2:
        print('YES')
    else:
        print('NO')
# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()
