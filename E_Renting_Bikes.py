
import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    n,m,a = [int(i) for i in input().split()]
    personal = [int(i) for i in input().split()]
    price = [int(i) for i in input().split()]

    personal.sort()
    price.sort()

    def dp(pri_i, per_i):
        if per_i > n:
            return [0,0,0]
        p = dp(pri_i + 1, per_i + 1)
        p_n = dp(pri_i, per_i + 1, )
    
        p[0] += 1
        p[0] += 

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
