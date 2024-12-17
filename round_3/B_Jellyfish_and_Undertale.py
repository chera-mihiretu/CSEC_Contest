from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    a,b,n = [int(i) for i in input().split()]
    tools = [int(i) for i in input().split()]
    answer = 0
    
    
    for i in range(n):
        answer += min(tools[i], a - 1)
    answer += b

    print(answer)


# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()