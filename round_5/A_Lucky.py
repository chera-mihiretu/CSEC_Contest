from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    string = [int(i) for i in list(input())]

    if (sum(string[:3]) == sum(string[3:])):
        print("YES")
    else:
        print("NO")
# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()