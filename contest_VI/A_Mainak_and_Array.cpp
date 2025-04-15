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

    int t; 
    cin >> t; 
    while (t--) {

        int n; 
        cin >>  n;

        vector<int> arr(n, 0);


        for (int i = 0;  i < n; i ++) cin >>  arr[i];
        
        int answer = 0; 

        for (int i = 0; i < n ; ++i) {
            answer = max(answer, arr[i] - arr[(i + 1) % n]);

        }
        int another = 0;
        if (n != 1){

            another = *max_element(arr.begin() + 1, arr.end()) - arr[0] ;
            another = max(another, arr[n - 1] - *min_element(arr.begin(), arr.end() - 1));
        }

        cout << max(another, answer) << endl;
    }

    return 0;
}
