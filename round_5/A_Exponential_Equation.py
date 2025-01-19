from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())

    if n & 1:
        print(-1)
        return 
    print(1, n // 2)



# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()