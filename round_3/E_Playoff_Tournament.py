from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()

class SegmentTree:
    def __init__(self, size, string):
        self.string = string
        self.size = size
        self.tree = [0] * (2 * self.size)
        self.build()
    def build(self):
        for i in range(self.size):
            self.tree[i + self.size] = 1
            
        for j in range(self.size - 1, -1, -1):
            self.setValue(j)

    def setValue(self, parent):
        
        if self.string[parent] == '0':
            self.tree[parent] = self.tree[parent << 1 | 1]
        elif self.string[parent] == '1':
            self.tree[parent] = self.tree[parent << 1]
        else:
            self.tree[parent] = self.tree[parent << 1] + self.tree[parent << 1 | 1]
    def update(self, index, command):
        self.string[index] = command
        while index >= 1:
            self.setValue(index)
            
            index >>= 1
    def getAnswer(self):
        return self.tree[1]



# solution
def solution():
    k = int(input())
    string =  input()
    string = ['0'] + list(string)[::-1]
    q = int(input())


    answer = []
    segented_tree = SegmentTree(pow(2, k), string)
    for _ in range(q):
        index, command = input().split()    
        segented_tree.update(pow(2, k) - int(index), command)
        # print(segented_tree.tree)
        answer.append(segented_tree.getAnswer())
    print(*answer, sep='\n')
    # segmented tree
        



# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()