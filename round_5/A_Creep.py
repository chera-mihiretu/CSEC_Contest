from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    i, j = [int(i) for i in input().split()]
    answer = []
    for k in range(i + j):
        if i:
            answer.append("0")
            i -= 1
        if j:
            answer.append("1")
            j -= 1
    print(*answer, sep="")

# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()