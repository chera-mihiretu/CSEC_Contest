#include <bits/stdc++.h> 
#define Arr(T) vector<int> 
#define Pair pair<int, int> 
using namespace std;

typedef long long ll;
class SegmentedTree{
private:
    Arr(ll) seg;
    Arr(ll) lazy;
    int n;
public:
    SegmentedTree(int n){
        this->n = n;
        this->seg.assign(n * 4, 0);
        this->lazy.assign(n * 4, 0);
    }

    Pair getMeChild(int node) {
        return Pair {node * 2 + 1, node * 2 + 2};
    }
    int query(int index){
        return this->privateQuery(0, 0, this->n - 1, index);
    }
    void update(int left, int right, int number){
        privateUpdate(0, 0, this->n - 1, left, right - 1, number);
    }
private:
    void privateUpdate(int node, int left, int right, int l, int r, int number) {
        Pair child = this->getMeChild(node);
        
        
        seg[node] = max(seg[node], lazy[node]);
        if (left != right) {
            lazy[child.first] = max(lazy[child.first],  lazy[node]);
            lazy[child.second] = max(lazy[child.second],  lazy[node]);
        }

        
        

        if (left > r || right < l) return; 

        if (left == l && right == r) {

            
            seg[node] = max(seg[node], number);
            if (left != right) {
                lazy[child.first] = max(lazy[child.first], number);
                lazy[child.second] = max(lazy[child.second], number);
            }
            
            return; 
        }
        int mid = left + (right - left ) / 2;
        privateUpdate(child.first, left, mid, l, min(r, mid), number);

        privateUpdate(child.second, mid + 1, right, max(mid + 1, l), r, number);

    }

    int privateQuery(int node, int left, int right, int index) {
        Pair child = this->getMeChild(node);
        seg[node] = max(seg[node], lazy[node]);
        if (left != right) {
            lazy[child.first] = max(lazy[child.first], seg[node]);
            lazy[child.second] = max(lazy[child.second], seg[node]);
        }
        
        if (left == right ) {
            return seg[node];
        }
        
        int mid = left + (right - left ) / 2;
        
        if (index <= mid) {
            return privateQuery(child.first, left, mid, index);
        }else {
            return privateQuery(child.second, mid + 1, right, index);
        }

        
    }
};

int main () {

    int n, m;
    cin >> n >> m;

    SegmentedTree* tree = new SegmentedTree(n);

    for (int i = 0; i < m; i ++) {
        int command;
        cin >> command;
        if (command == 1) {

            int l, r, number;

            cin >> l >> r >> number ;

            tree->update(l , r , number);

        }else {
            int index;
            cin >> index;
        

            cout << tree->query(index) << endl;

        }
    } 
    
}    