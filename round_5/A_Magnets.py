from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    prev = "88"
    group = 0
    for _ in range(n):
        side = input()
        if side[0] == prev[-1]:
            group += 1
        prev = side
    print(group + 1)


# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()