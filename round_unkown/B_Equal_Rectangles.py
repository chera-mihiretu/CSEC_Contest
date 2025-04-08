from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution


def solution():
    n = int(input())
    nums = [int(i) for i in input().split()]

    nums.sort()

    start, _start,  end, _end = 0,1, len(nums) - 1, len(nums) - 2

    prev = -1
 
    while start < end:
        if nums[start] != nums[_start] or nums[end] != nums[_end]:
            return print("NO")
        if  prev == -1:
            prev = nums[start] * nums[end]
        else:
            if prev != nums[start] * nums[end]:
                print('NO')
                break
        start += 2
        end -= 2
        _end -= 2
        _start += 2
    else:
        print("YES")

    
# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()