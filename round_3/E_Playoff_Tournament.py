
import sys, threading



input = lambda: sys.stdin.readline().strip()


class SegmentedTree:
    def __init__(self, k, string):
        self.string = string
        self.k = k
        self.tree = [0] * (pow(2, k) * 4)
        self.build()
    def build(self):    
        # print(self.string)
        self._build(0, 0, pow(2, self.k) - 1, 0)



    def _build(self, node, left, right, index):
        if left == right:
            self.tree[node] = 1
            return 
        mid = (left + right) // 2
        left_child, right_child = self.getChild(node)
        left_index, right_index = self.getChild(index)
        self._build(left_child, left, mid, left_index)
        self._build(right_child, mid + 1, right, right_index)
        if self.string[index] == '1':
            self.tree[node] = self.tree[left_child]
        elif self.string[index] == '0':
            self.tree[node] = self.tree[right_child]
        else:
            self.tree[node] = self.tree[right_child] + self.tree[left_child]
        
        
    def modifyIndex(self, node, path, index):
        left_child, right_child = self.getChild(node)
        if index == 0:
            if self.string[path[index]] == '1':
                self.tree[node] = self.tree[left_child]
            elif self.string[path[index]] == '0':
                self.tree[node] = self.tree[right_child]
            else:
                self.tree[node] = self.tree[right_child] + self.tree[left_child]
            return
        
        
        
        if path[index - 1] == left_child:
            self.modifyIndex(left_child, path, index - 1)
        else:
            self.modifyIndex(right_child, path, index - 1)


        if self.string[path[index]] == '1':
            self.tree[node] = self.tree[left_child]
        elif self.string[path[index]] == '0':
            self.tree[node] = self.tree[right_child]
        else:
            self.tree[node] = self.tree[right_child] + self.tree[left_child]

    def getPath(self, index, command):
        self.string[index] = command
        path = []
        while index: 
            path.append(index)
            index = (index - 1) // 2
        path.append(0)
        
        self.modifyIndex(0, path, len(path) - 1)  

    def getChild(self, node):
        return node * 2 + 1, node * 2 + 2
def main():
    k = int(input())
    string = list(input())[::-1]
    query = int(input())

    segmented = SegmentedTree(k, string)
    answer = []
    # answer.append(segmented.tree[0])

    for _ in range(query):
        index, command = input().split()
        index = int(index)
        
        segmented.getPath((-index % len(string)), command)
        
        answer.append(segmented.tree[0])
        
        
    print(*answer, sep='\n')
    
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
