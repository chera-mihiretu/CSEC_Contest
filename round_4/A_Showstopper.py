from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())

    nums1 = [int(i) for i in input().split()]
    nums2 = [int(i) for i in input().split()]
    answer = False
    answer |= doTheJob(n, nums1[::], nums2[::])
    nums1[n-1],nums2[n-1] = nums2[n-1],nums1[n-1]
    answer |= doTheJob(n, nums2[::], nums1[::])

    if answer:
        print("Yes")
    else:
        print("No")
    
    
def doTheJob(n, a, b):
    for i in range(n - 1):
        if a[i] > a[n - 1]:
            a[i],b[i] = b[i],a[i]
        if b[i] > b[n - 1]:
            a[i],b[i] = b[i],a[i]
    max_a = max(a)
    max_b = max(b)

    if max_a == a[n-1] and max_b == b[n-1]:
        return True
    return False

    

            
    

# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()