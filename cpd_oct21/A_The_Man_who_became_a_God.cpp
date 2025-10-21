// lucky me 
#include <bits/stdc++.h>
#define all(arr) arr.begin(), arr.end()
#define Arr(T) vector<T> 
using namespace std;    
int main () {
    int t;
    cin >> t;
    while (t--) {
        int n, k;
        cin >> n >> k;




        Arr(int) arr(n);

        for (int i = 0; i < n; i ++) cin >> arr[i];


        Arr(int) pre;

        for (int i = 1; i < n; i ++) {
            pre.push_back(abs(arr[i] - arr[i -1]));
        }

        sort(all(pre));
        int answer= 0;


        // for (auto a : pre) cout << a << ' ';
        // cout << endl;

        for (int i = 0; i < (n - k) ; i++) {
            answer += pre[i];
        }

        cout << answer << endl;

    }
}