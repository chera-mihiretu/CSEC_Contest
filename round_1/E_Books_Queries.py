from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()

"""
L 1
R 2
R 3
? 2
L 4
? 1
L 5
? 1

  1       2       3      4
[[0,0], [1,0], [2, 0], [0,3], [0,4]]
   1      1       1      2     3
   0      1       2      2     2


1
1
2
    

"""
# solution
def solution():
    q = int(input())

    left_pre = [0]
    right_pre = [0]
    array = []
    nums_pos = {}
    answer = []
    for _ in range(q):
        command, number = input().split()
        if command == '?':
            index = nums_pos[number] 
      
            left = array[index-1][0] + (left_pre[-1] - left_pre[index] )
            right = array[index-1][1] + (right_pre[-1] - right_pre[index])
            answer.append(min(left, right))
        else:
            
            if command == 'L':
                array.append([0, len(array)])
                left_pre.append(left_pre[-1] + 1)
                right_pre.append(right_pre[-1])
            else:
                array.append([len(array), 0])
                right_pre.append(right_pre[-1] + 1)
                left_pre.append(left_pre[-1])
            nums_pos[number] = len(array) 
    
    # print(left_pre, right_pre, array, sep='\n')
    print(*answer, sep='\n')
        

# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()