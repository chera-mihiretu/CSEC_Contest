// lucky me 
#include <bits/stdc++.h>
#define all(arr) arr.begin(), arr.end()
#define Arr(T) vector<T> 
#define Pair(T) pair<int,int>
#define f first
#define s second

using namespace std;    
typedef long long ll;
int solve () {

    function<ll(ll, ll)> getMeSum = [](ll from, ll to ) -> ll {
        return ((to - from + 1) * (from + to)) / 2;
    };
   

    ll k, x;
    cin >> k >> x;

    if (getMeSum(1, k) + getMeSum(1, k -1) < x) {
        return k * 2 - 1;
    }

    

    ll start = 0;
    ll end = k * 2;

    ll answer = 0;

    while (start <= end) {
        ll mid = start + (end - start) / 2;
        ll s;

        
        if (mid > k) {
            s = getMeSum(1, k) + getMeSum((k-1) - (mid - k) + 1, k-1);
        } else {
            s = getMeSum(1, mid);
        }
        // cout << mid << ' ' << s<< endl;
        
        if (s < x) {
            start = mid + 1;
            answer = mid + 1;
        } else {
            end = mid - 1;
        }
    }

    return answer;


    

}
int main () {

    int t;
    cin >> t;
    while (t--)
        cout << solve() << endl;

    
    

    

}