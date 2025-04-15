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
        int d, sumTime;

        scanf("%d %d", &d, &sumTime);

        vector<pair<int, int>> arr(d, pair<int, int>());
        int minimum = 0, maximum = 0;

        for (int i = 0; i < d; ++i) {
            scanf("%d %d", &arr[i].F, &arr[i].S);
             minimum += arr[i].F;
             maximum += arr[i].S;
        }

        if (minimum > sumTime || maximum < sumTime) {
            printf("NO\n");
        }else {
            vector<int> pref(d, 0);
            pref[d-1] = arr[d-1].F;

            for (int i = d - 2; i >= 0; i--) {
                pref[i] = pref[i + 1] + arr[i].F;
            }

            vector<int> ans;
            

            for (int i = 0; i < d - 1 ; i ++) {
                int current = min(arr[i].S, sumTime - pref[i + 1]);

                sumTime -= current;

                ans.push_back(current);

            }
            ans.push_back(sumTime);

            printf("YES\n");

            for (int i = 0; i < d; i++) {
                printf("%d ", ans[i]);
            }
            printf("\n");

        }

        


        
    }

    return 0;
}
