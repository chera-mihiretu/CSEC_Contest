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
    while (t--) {
        int n;  
        scanf("%d", &n);
        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            scanf("%d", &a[i]);
        }

        unordered_map<int, int> count;

        int temp = 0;
        for (int i = 0; i < a.size(); ++i) {
            temp = min(temp, a[i]);
        }

        vector<int> divs;

        auto add = [](unordered_map<int, int>& c, int n){
            if (c.find(n) == c.end()) {
                c[n] = 0;
            }
            c[n]++;
        };


        for (int i = 0; i < n; ++i) {
            int temp = a[i];
            int d = 2;
            add(count, a[i]);

            if ((a[i] & 1) == 0) {
                add(count, a[i]/2);
            }

            while (d * d <= temp) {
                if (temp % d == 0) {
                    count[d]++;   
                }
                d++;
            }
        }

        int answer = 1;

        for (auto [a,b] : count) {
            if (b == n) answer ++;
        }

        
        printf("%d\n", answer);
        
    }

    return 0;
}
