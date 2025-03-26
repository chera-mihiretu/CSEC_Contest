from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    
    s = input()

    s = [int(i) for i in s]
    n = len(s)
    for i in range(n):

        while   i > 0 and s[i] - 1 > s[i-1]:
            s[i], s[i-1] = s[i-1],s[i]
            s[i-1] -=1
            i -= 1
    print(*s, sep="")


# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()