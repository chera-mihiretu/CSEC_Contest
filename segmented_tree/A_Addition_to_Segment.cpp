#include <bits/stdc++.h> 
#define Arr(T) vector<ll> 
#define Pair pair<ll, ll> 
using namespace std;

typedef long long ll;
class SegmentedTree{
private:
    Arr(ll) seg;
    Arr(ll) lazy;
    ll n;
public:
    SegmentedTree(ll n){
        this->n = n;
        this->seg.assign(n * 4, 0);
        this->lazy.assign(n * 4, 0);
    }

    Pair getMeChild(ll node) {
        return Pair {node * 2 + 1, node * 2 + 2};
    }
    ll query(ll index){
        return this->privateQuery(0, 0, this->n - 1, index);
    }
    void update(ll left, ll right, ll number){
        privateUpdate(0, 0, this->n - 1, left, right - 1, number);
    }
private:
    void privateUpdate(ll node, ll left, ll right, ll l, ll r, ll number) {
        Pair child = this->getMeChild(node);
        if (lazy[node] != 0) {
            seg[node] += lazy[node] * (right - left + 1);
            if (left != right) {
                lazy[child.first] += lazy[node];
                lazy[child.second] += lazy[node];
            }
            lazy[node] = 0;
        }

        if (left > r || right < l) return; 

        if (left == l && right == r) {

            
            seg[node] += (number) * (right - left + 1);
            if (left != right) {
                lazy[child.first] += number;
                lazy[child.second] += number;
            }
            
            return; 
        }
        ll mid = left + (right - left ) / 2;
        privateUpdate(child.first, left, mid, l, min(r, mid), number);

        privateUpdate(child.second, mid + 1, right, max(mid + 1, l), r, number);

    }

    ll privateQuery(ll node, ll left, ll right, ll index) {
        Pair child = this->getMeChild(node);
        if (lazy[node] != 0) {
            seg[node] += lazy[node] * (right - left + 1);
            if (left != right) {
                lazy[child.first] += lazy[node];
                lazy[child.second] += lazy[node];
            }
            lazy[node] = 0;
        }
        
        if (left == right ) {
            return seg[node];
        }
        
        ll mid = left + (right - left ) / 2;
        
        if (index <= mid) {
            return privateQuery(child.first, left, mid, index);
        }else {
            return privateQuery(child.second, mid + 1, right, index);
        }

        
    }
};

int main () {

    ll n, m;
    cin >> n >> m;

    SegmentedTree* tree = new SegmentedTree(n);

    for (ll i = 0; i < m; i ++) {
        ll command;
        cin >> command;
        if (command == 1) {

            ll l, r, number;

            cin >> l >> r >> number ;

            tree->update(l , r , number);

        }else {
            ll index;
            cin >> index;
        

            cout << tree->query(index) << endl;

        }
    } 
    
}    