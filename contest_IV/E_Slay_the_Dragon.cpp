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
    // cin >> t; 
    while (t--) {
        int n, m;
        cin >> n; 
        vector<ll> arr(n, 0);

        for (int i = 0; i < n; i++) cin >> arr[i];
        ll total = accumulate(all(arr), 0LL);
        sort(all(arr));

        vector<ll> answer;

        cin >> m;
        while (m--) {

            ll defence, attack;
            cin >> defence >> attack;

            int i = lower_bound(all(arr), defence) - arr.begin();

            ll coin = LLONG_MAX;

            if (i > 0) coin = min(coin, (defence - arr[i-1]) + max(0LL, attack - total + arr[i-1]));
            if (i < n) coin = min(coin, max(0LL, max(0LL, attack - total + arr[i])));
            answer.pb(coin);

        }



        
        for (auto ans : answer) cout << ans << endl;


    }

    return 0;
}
