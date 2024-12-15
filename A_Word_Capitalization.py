from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    string = input()
    li = string.split()
    answer = []
    for i in li:
        if i[0].isupper():
            answer.append(i)
        else:
            answer.append(i[0].upper() + i[1:])
    print(' '.join(answer))


# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()

