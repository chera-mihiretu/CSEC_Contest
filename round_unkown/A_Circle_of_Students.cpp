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

    int t ; 
    scanf("%d", &t);
    while (t--) {
        int n;
        scanf("%d", &n);
        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            scanf("%d", &a[i]);
            
        } 
        int one = -1;
        for (int i =0; i < n; i ++) {
            if (a[i] == 1) {
                one = i;
                break;
            }
        }

        int flag = true;
        int m = n - 1;
        int i = one;
        while (m--){
            if (a[i % n] != (a[(i + 1) % n] - 1)){
                flag = false;
            }
            i ++;
        }
        
        
        if (flag) {
            printf("YES\n");
            continue;
        }
        flag = true;
        m = n - 1;
        i = one;
        while (m--) {
            if (a[(i + n) % n] != (a[((i - 1) + n) % n] - 1)){
                flag = false;
            }
            i --;
        }

        if (flag) {
            printf("YES\n");
            continue;
        }
        printf("NO\n");
       
        
    }

    return 0;
}
