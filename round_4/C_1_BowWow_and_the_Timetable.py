from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    s = input()

    end = len(s) - 1
    answer = 0
    total = sum([int(i) for i in list(s)])
    while end >= 0:
        if end != 0 or total > 1:
            answer += 1
        end -= 2

    print(answer)

# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()