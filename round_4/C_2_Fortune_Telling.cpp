#include <bits/stdc++.h> 
using namespace std;


#define ll long long
#define pb push_back
#define all(v) v.begin(), v.end()
#define rall(v) v.rbegin(), v.rend()
#define F first
#define S second
#define endl '\n'

const ll MOD = 1e9 + 7;
const ll INF = 1e18;


void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
}


int main() {
    fastIO();

    int t = 1; 
    cin >> t; 
    while (t--) {
        
        ll n, a, y;
        cin >> n >> a >> y;

        vector<ll> nums(n);
        
        for (int i = 0; i < n; ++i ) cin >> nums[i];

        ll total = accumulate(all(nums), 0);

        if ((total + a + y ) & 1) {
            cout << "Bob" << endl;
        }else{
            cout << "Alice" << endl;
        }
        
    }

    return 0;
}